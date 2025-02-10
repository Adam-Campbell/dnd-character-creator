import json
import environ
import cloudinary.uploader
import cloudinary.exceptions
from django.shortcuts import render, get_object_or_404, redirect
from django.http import (
    HttpResponse,
    JsonResponse,
    HttpResponseForbidden,
    HttpResponseNotFound
)
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views import generic
from openai import OpenAI
from .models import Character
from .forms import CharacterForm
from .data_utils import (
    get_static_data,
    get_item_by_id,
    format_line_breaks,
    get_image_url
)


env = environ.Env(
    ENABLE_IMAGE_GENERATION=(bool, False)
)


def get_image_generation_enabled_status():
    return env('ENABLE_IMAGE_GENERATION')


client = OpenAI()


class CharacterList(generic.ListView):
    """
    Renders a paginated list of all characters that are either public,
    or belong to the currently logged in user.
    Accepts optional query parameters for filtering the results.
    Returns 12 characters per page in order to work nicely with the
    character grid layout.
    """
    model = Character
    template_name = 'characters/character_list.html'
    context_object_name = 'characters'
    paginate_by = 12

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            queryset = (
                Character.objects.filter(is_public=True)
                | Character.objects.filter(user=user)
            )
        else:
            queryset = Character.objects.filter(is_public=True)
        character_class = self.request.GET.get('character_class')
        race = self.request.GET.get('race')
        if character_class:
            queryset = queryset.filter(character_class=character_class)
        if race:
            queryset = queryset.filter(race=race)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        characters = context['characters']
        # Enrich each character with additional properties
        static_data = get_static_data()
        for character in characters:
            character.image = get_image_url(character.image.public_id)
            character.class_data = get_item_by_id(
                static_data['classes'],
                str(character.character_class)
            )
            character.race_data = get_item_by_id(
                static_data['races'],
                str(character.race)
            )
            character.user.userprofile.image = get_image_url(
                character.user.userprofile.image.public_id,
                width=60,
                height=60
            )
        return context


@login_required
def create_character(request):
    """
    Handles requests related to new character creation.

    GET - Renders the character_editor.html template, containing the
    character editor.

    POST - Creates a new character based on the JSON data received in the
    request body.

    """
    if request.method == 'POST':
        try:
            character_data = json.loads(request.body)
            form = CharacterForm(character_data)
            if form.is_valid():
                try:
                    new_character = form.save(commit=False)
                    new_character.user = request.user
                    new_character.image = character_data['image']
                    new_character.save()
                    request.user.liked_characters.add(new_character)
                    return JsonResponse({
                        'message': 'POST request handled',
                        'characterId': new_character.id
                    })
                except Exception as e:
                    print(f"An error occurred: {e}")
                    return JsonResponse(
                        {
                            'message': f'An error occurred: {e}'
                        },
                        status=500
                    )
            else:
                print("FORM INVALID")
                return JsonResponse(
                    {'message': 'Invalid character data'},
                    status=400
                )

        except json.JSONDecodeError:
            # If JSON data malformed, return a 400 error
            return JsonResponse({'message': 'Invalid JSON data'}, status=400)
        except KeyError as e:
            # If a required key is missing, return a 400 error
            return JsonResponse({'message': f'Missing key: {e}'}, status=400)
        except Exception as e:
            return JsonResponse(
                {'message': f'An error occurred: {e}'},
                status=500
            )
    # End of POST request handling
    editor_data = json.dumps({
        'editingContext': 'CREATE_NEW',
        'characterId': None,
        'characterData': None,
        'enableImageGeneration': get_image_generation_enabled_status()
    })
    return render(request, 'characters/character_editor.html', {
        'editor_data': editor_data
    })


@login_required
def edit_character(request, id):
    """
    Handles requests related to editing an existing character.

    GET - Renders the character_editor.html template, containing the character
    editor. Passes the character data to the template.

    POST - Updates the character based on the JSON data received in the
    request body.
    """
    if request.method == 'POST':
        character_data = json.loads(request.body)
        character = Character.objects.get(id=id)
        form = CharacterForm(character_data, instance=character)
        if form.is_valid():
            character.image = character_data['image']
            form.save()
            return JsonResponse({'message': 'Character updated successfully'})
        else:
            return JsonResponse(
                {'message': 'Invalid character data'},
                status=400
            )
    # End of POST request handling
    try:
        character = Character.objects.get(id=id)
    # If the character does not exist, return a 404 error
    except Character.DoesNotExist:
        return HttpResponseNotFound("Character does not exist")
    # If the character does not belong to the user, return a 403 error
    if character.user != request.user:
        return HttpResponseForbidden(
            "You do not have permission to edit this character"
        )
    # If the character exists and belongs to the user, render the
    # edit_character.html template
    editor_data = json.dumps({
        'editingContext': 'EDIT_EXISTING',
        'characterId': id,
        'characterData': character.to_json(),
        'enableImageGeneration': get_image_generation_enabled_status()
    })
    return render(request, 'characters/character_editor.html', {
        'editor_data': editor_data
    })


@login_required
def clone_character(request, character_id):
    """
    Clone an existing character. If the character exists and the user has
    the required permissions, render the character_editor.html template with
    the character data.
    """
    character = get_object_or_404(Character, id=character_id)
    if not character.is_public and character.user != request.user:
        return HttpResponseForbidden(
            "You do not have permission to clone this character"
        )
    character_copy = character.to_json(exclude_id=True)
    editor_data = json.dumps({
        'editingContext': 'CLONE_EXISTING',
        'characterId': None,
        'characterData': character_copy,
        'enableImageGeneration': get_image_generation_enabled_status()
    })
    return render(request, 'characters/character_editor.html', {
        'editor_data': editor_data
    })


def character_detail(request, id):
    """
    Renders the detailed view for a single character.
    If the character is not public and does not belong to the user, return a
    403 error.
    Before rendering the template, enrich the character object with additional
    properties.
    """
    # Get character object from database
    character = get_object_or_404(Character, id=id)
    # If the character is not public and does not belong to the user,
    # return a 403 error
    if not character.is_public and character.user != request.user:
        return HttpResponseForbidden(
            "You do not have permission to view this character"
        )
    user_has_liked = character.liked_by.filter(id=request.user.id).exists()
    user_is_owner = character.user == request.user
    # Get static data and add the relevant class and race data to the
    # character object
    character.image = get_image_url(character.image.public_id)
    character.user.userprofile.image = get_image_url(
        character.user.userprofile.image.public_id,
        width=60,
        height=60
    )
    static_data = get_static_data()
    character.class_data = get_item_by_id(
        static_data['classes'],
        str(character.character_class)
    )
    character.race_data = get_item_by_id(
        static_data['races'],
        str(character.race)
    )
    # Format skill and spell choices
    character.character_class_skill_choices = [
        get_item_by_id(static_data['skills'], skill_id)
        for skill_id in character.character_class_skill_choices
    ]
    character.character_class_cantrip_choices = [
        get_item_by_id(static_data['spells'], cantrip_id)
        for cantrip_id in character.character_class_cantrip_choices
    ]
    character.character_class_spell_choices = [
        get_item_by_id(static_data['spells'], spell_id)
        for spell_id in character.character_class_spell_choices
    ]
    for cantrip in character.character_class_cantrip_choices:
        cantrip['description'] = format_line_breaks(cantrip['description'])
    for spell in character.character_class_spell_choices:
        spell['description'] = format_line_breaks(spell['description'])
    # Format ability points
    temp_abilities = []
    for abilityValue in character.ability_points:
        ability_id = abilityValue['id']
        base_value = abilityValue['value']
        ability = get_item_by_id(static_data['abilities'], ability_id)
        racial_bonus = 0
        for b in character.race_data['abilityBonuses']:
            if b['ability']['id'] == ability['id']:
                racial_bonus = b['bonus']
                break
        derived_value = base_value + racial_bonus
        modifier = (derived_value - 10) // 2
        temp_abilities.append({
            'ability': ability,
            'base_value': base_value,
            'racial_bonus': racial_bonus,
            'derived_value': derived_value,
            'modifier': modifier
        })
    character.ability_points = temp_abilities

    # Combine the weapon proficiencies from race and class into a single list
    # and de-duplicate them
    weapon_proficiencies = list(
        {
            weapon['id']: weapon
            for weapon in (
                character.race_data['weaponProficiencies']
                + character.class_data['proficiencies']['weapons']
            )
        }.values()
    )
    character.class_data['proficiencies']['weapons'] = weapon_proficiencies

    return render(request, 'characters/character_detail.html', {
        'character': character,
        'user_has_liked': user_has_liked,
        'user_is_owner': user_is_owner,
        'id': id,
        'is_logged_in': request.user.is_authenticated
    })


@login_required
def toggle_like(request, character_id):
    """
    Toggles the 'like' status of a character for the currently logged in user,
    if the user has the required permissions.

    After performing the operation, redirect the user to the character detail
    page. This behaviour is because the only current way to like a character
    is by clicking the like button on the character detail page. If that
    changes in the future, this function may need to be updated.
    """
    character = get_object_or_404(Character, id=character_id)
    # If the character is not public and does not belong to the user,
    # return a 403 error
    if not character.is_public and character.user != request.user:
        return HttpResponseForbidden(
            "You do not have permission to like this character"
        )
    if request.user.liked_characters.filter(id=character_id).exists():
        request.user.liked_characters.remove(character)
    else:
        request.user.liked_characters.add(character)
    return redirect('characters:character_detail', id=character_id)


@login_required
def toggle_privacy(request, character_id):
    """
    Toggles the privacy status of a character, via its is_public field, as
    long as the current user has the required permissions.

    After performing the operation, redirect the user to the character detail
    page. This behaviour is because the only current way to change the privacy
    of a character is by clicking the appropriate button on the character
    detail page. If that changes in the future, this function may need to be
    updated.
    """
    character = get_object_or_404(Character, id=character_id)
    if character.user != request.user:
        return HttpResponseForbidden(
            (
                "You do not have permission to change the privacy of this "
                "character"
            )
        )
    character.is_public = not character.is_public
    character.save()
    return redirect('characters:character_detail', id=character_id)


@login_required
@require_http_methods(['DELETE'])
def delete_character(request, character_id):
    """
    Deletes a character from the database, as long as the current user has the
    required permissions.
    Returns a 204 status code if the operation is successful.
    """
    character = get_object_or_404(Character, id=character_id)
    if character.user != request.user:
        return HttpResponseForbidden(
            "You do not have permission to delete this character"
        )
    character.delete()
    return HttpResponse(status=204)


@login_required
def upload_image(request):
    if request.method == 'POST':
        try:
            image = request.FILES['image']

            if not image:
                return JsonResponse(
                    {'message': 'No image provided'},
                    status=400
                )

            response = cloudinary.uploader.upload(image)
            return JsonResponse({
                'url': response['secure_url'],
                'id': response['public_id']
            })

        except cloudinary.exceptions.Error as e:
            return JsonResponse(
                {'message': f'An error occurred: {e}'},
                status=500
            )


@login_required
def generate_image(request):
    if request.method == 'POST':
        if not get_image_generation_enabled_status():
            return JsonResponse(
                {'message': 'Image generation is disabled'},
                status=403
            )
        print("Generating image...")
        # Grab the structured character data from the request body
        character_data = json.loads(request.body)
        # This prompt is fed to an LLM to turn the structured charactr data
        # into natural language
        conversion_instructions = (
            "Your goal is to take structured data describing a Dungeons and "
            "Dragons character, and convert it into a natural language "
            "description of the character including their race, class, and "
            "physical features. Here is the structured data: "
        )
        llm_natural_language_conversion_prompt = f"""
        {conversion_instructions}
        {str(character_data)}
        """
        # Send prompt to OpenAI's LLM
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "developer",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": llm_natural_language_conversion_prompt
                }
            ]
        )
        # Extract the natural language character description from the
        # completion
        natural_language_character_description = (
            completion.choices[0].message.content
        )
        # This is a preset style instruction for the DALL-E model
        style_instructions = (
            "Artwork of a fantasy character, single full-body artwork. The "
            "image must use a classic hand-painted high-fantasy illustration "
            "style. The image must not include multiple versions of the "
            "character, or any text or watermarks. It must just include a "
            "single character, who is the focal point of the image."
        )
        # Construct the DALL-E image prompt by combining the style
        # instructions and the natural language character description
        dalle_image_prompt = f"""
        {style_instructions}
        {natural_language_character_description}
        """
        # Send the prompt to OpenAI's DALL-E model
        response = client.images.generate(
            prompt=dalle_image_prompt,
            model='dall-e-3',
            n=1,
            response_format="url",
            size="1024x1024",
            style="vivid"
        )
        # Extract the image URL from the response
        dalle_image_url = response.data[0].url
        # If the image URL is valid, upload the image to Cloudinary and
        # return the URL
        if dalle_image_url:
            cloudinary_response = cloudinary.uploader.upload(dalle_image_url)
            cloudinary_image_url = cloudinary_response['secure_url']
            if cloudinary_image_url:
                return JsonResponse({
                    'url': cloudinary_image_url,
                    'id': cloudinary_response['public_id']
                })
        return JsonResponse({'message': 'An error occurred'}, status=500)
