import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from characters.models import Character
from characters.data.characters_data import (
    users_data_list,
    characters_data_list
)


class Command(BaseCommand):
    help = 'Create users and characters to populate the database.'

    def handle(self, *args, **kwargs):
        # Delete all characters
        Character.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Deleted all characters.'))

        # Delete all users except for the superuser
        User.objects.filter(is_superuser=False).delete()
        self.stdout.write(
            self.style.SUCCESS('Deleted all users except for the superuser.')
        )

        # Create the users
        for user_data in users_data_list:
            user = User.objects.create_user(
                username=user_data['username'],
                password=user_data['password']
            )
            user.userprofile.bio = user_data['bio']
            user.userprofile.image = user_data['image']
            user.userprofile.save()
            self.stdout.write(
                self.style.SUCCESS(f'User {user.username} created with bio.')
            )

        users = User.objects.filter(is_superuser=False)
        if not users:
            self.stdout.write(
                self.style.ERROR('No users found in the database.')
            )
            return

        for character_data in characters_data_list:
            user = random.choice(users)
            character = Character.objects.create(
                user=user,
                **character_data
            )
            self.stdout.write(
                self.style.SUCCESS(f'Character {character.name} created.')
            )

        self.stdout.write(
            self.style.SUCCESS('Successfully created characters.')
        )

        # Add likes
        characters = Character.objects.all()
        for user in users:
            # Random number of likes for each user
            n = random.randint(1, len(characters))
            liked_characters = random.sample(list(characters), n)
            for character in liked_characters:
                character.liked_by.add(user)
                self.stdout.write(self.style.SUCCESS(
                    f'User {user.username} liked character {character.name}.')
                )

        self.stdout.write(self.style.SUCCESS('Successfully added likes.'))
