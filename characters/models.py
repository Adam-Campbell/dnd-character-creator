import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from cloudinary.models import CloudinaryField


class Character(models.Model):

    ALIGNMENT_CHOICES = [
        ('Lawful Good', 'Lawful Good'),
        ('Neutral Good', 'Neutral Good'),
        ('Chaotic Good', 'Chaotic Good'),
        ('Lawful Neutral', 'Lawful Neutral'),
        ('True Neutral', 'True Neutral'),
        ('Chaotic Neutral', 'Chaotic Neutral'),
        ('Lawful Evil', 'Lawful Evil'),
        ('Neutral Evil', 'Neutral Evil'),
        ('Chaotic Evil', 'Chaotic Evil'),
    ]

    CHARACTER_CLASS_CHOICES = [
        (uuid.UUID('44f84547-8935-4ab4-bd29-fb60d0000d04'), 'Barbarian'),
        (uuid.UUID('ea6fbdc2-82c7-44d7-b065-bd70e136ccc7'), 'Bard'),
        (uuid.UUID('17d2bd00-57b7-4756-b14e-43bf1f102585'), 'Cleric'),
        (uuid.UUID('e72b02b5-a7d0-4b1b-860f-7c965ea5e18c'), 'Fighter'),
        (uuid.UUID('32ea43f0-8f6f-4ce4-829c-f58955a758d1'), 'Rogue'),
        (uuid.UUID('ef560074-395d-4e42-b5ac-5ad9d3342271'), 'Wizard'),
    ]

    CHARACTER_RACE_CHOICES = [
        (uuid.UUID('095914ea-d0a5-41dd-a003-6b5d4558a3ad'), 'Dwarf'),
        (uuid.UUID('576c1e3a-8464-4c1a-bbe7-3dde6813bbd3'), 'Elf'),
        (uuid.UUID('bf3b0c49-80cc-4258-85a0-3974f656469a'), 'Halfling'),
        (uuid.UUID('4725316c-cfc5-44a2-a69f-563088dec352'), 'Human'),
        (uuid.UUID('ec1f0336-fb41-4ac8-b1f3-2a574ddb1bd5'), 'Half-Elf'),
        (uuid.UUID('8b5c75dd-3d4f-41b4-a7c2-ec516f02256e'), 'Tiefling'),
    ]

    HAIR_LENGTH_CHOICES = [
        ('Bald', 'Bald'),
        ('Cropped', 'Cropped'),
        ('Short', 'Short'),
        ('Medium', 'Medium'),
        ('Long', 'Long'),
    ]

    HAIR_TYPE_CHOICES = [
        ('Straight', 'Straight'),
        ('Wavy', 'Wavy'),
        ('Curly', 'Curly'),
        ('Coily', 'Coily'),
    ]

    FACIAL_HAIR_STYLE_CHOICES = [
        ('None', 'None'),
        ('Stubble', 'Stubble'),
        ('Full Beard', 'Full Beard'),
        ('Goatee', 'Goatee'),
        ('Moustache', 'Moustache'),
        ('Sideburns', 'Sideburns'),
        ('Soul Patch', 'Soul Patch'),
        ('Mutton Chops', 'Mutton Chops'),
    ]

    FACIAL_HAIR_LENGTH_CHOICES = [
        ('Short', 'Short'),
        ('Medium', 'Medium'),
        ('Long', 'Long'),
    ]

    EYE_SHAPE_CHOICES = [
        ('Almond', 'Almond'),
        ('Round', 'Round'),
        ('Hooded', 'Hooded'),
        ('Monolid', 'Monolid'),
        ('Upturned', 'Upturned'),
        ('Downturned', 'Downturned'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    race = models.UUIDField(choices=CHARACTER_RACE_CHOICES)
    character_class = models.UUIDField(choices=CHARACTER_CLASS_CHOICES)
    character_class_skill_choices = models.JSONField(default=list)
    character_class_cantrip_choices = models.JSONField(
        default=list,
        blank=True
    )
    character_class_spell_choices = models.JSONField(default=list, blank=True)
    ability_points = models.JSONField(default=list)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=100)
    alignment = models.CharField(max_length=100, choices=ALIGNMENT_CHOICES)
    background = models.TextField()
    traits = models.JSONField(default=list, blank=True)
    ideals = models.JSONField(default=list, blank=True)
    bonds = models.JSONField(default=list, blank=True)
    flaws = models.JSONField(default=list, blank=True)
    height = models.CharField(max_length=100)
    build = models.CharField(max_length=100)
    skin_tone = models.CharField(max_length=100)
    hair_color = models.CharField(max_length=100)
    hair_style = models.CharField(max_length=100)
    hair_length = models.CharField(max_length=100, choices=HAIR_LENGTH_CHOICES)
    hair_type = models.CharField(max_length=100, choices=HAIR_TYPE_CHOICES)
    facial_hair_style = models.CharField(
        max_length=100,
        choices=FACIAL_HAIR_STYLE_CHOICES
    )
    facial_hair_length = models.CharField(
        max_length=100,
        choices=FACIAL_HAIR_LENGTH_CHOICES,
        blank=True
    )
    eye_color = models.CharField(max_length=100)
    eye_shape = models.CharField(max_length=100, choices=EYE_SHAPE_CHOICES)
    distinguishing_features = models.CharField(max_length=300, blank=True)
    clothing_style = models.CharField(max_length=200)
    clothing_colors = models.CharField(max_length=200)
    clothing_accessories = models.CharField(max_length=200, blank=True)
    image = CloudinaryField(
        'image',
        blank=True,
        default="fantasy-placeholder_tq6d9i"
    )
    liked_by = models.ManyToManyField(User, related_name='liked_characters')
    created_at = models.DateTimeField(default=now, editable=False)
    is_public = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def to_json(self, exclude_id=False):
        """
        Return a JSON representation of the instance. with populated fields
        such as class and race.
        """
        excluded_fields = {'user', 'liked_by', 'created_at'}
        if exclude_id:
            excluded_fields.add('id')
        instance_dict = {}
        for field in self._meta.fields:
            value = getattr(self, field.name)
            if field.name in excluded_fields:
                continue
            elif isinstance(field, models.UUIDField):
                instance_dict[field.name] = str(value)
            elif field.name == 'image':
                instance_dict['image'] = {
                    'url': self.image.url,
                    'id': self.image.public_id
                }
            else:
                instance_dict[field.name] = value
        return instance_dict

    def __str__(self):
        return self.name
