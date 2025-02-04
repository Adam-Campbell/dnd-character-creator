from django.core.management.base import BaseCommand
from characters.models import Character
from django.contrib.auth.models import User
from characters.data.characters_data import users_data_list, characters_data_list
import random



class Command(BaseCommand):
    help = 'Create users and characters to populate the database.'

    def handle(self, *args, **kwargs):
        # Delete all characters
        Character.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Deleted all characters.'))

        # Delete all users except for the superuser
        User.objects.filter(is_superuser=False).delete()
        self.stdout.write(self.style.SUCCESS('Deleted all users except for the superuser.'))

        # Create the users
        for user_data in users_data_list:
            user = User.objects.create_user(username=user_data['username'], password=user_data['password'])
            user.userprofile.bio = user_data['bio']
            user.userprofile.save()
            self.stdout.write(self.style.SUCCESS(f'User {user.username} created with bio.'))

        users = User.objects.filter(is_superuser=False)
        if not users:
            self.stdout.write(self.style.ERROR('No users found in the database.'))
            return
        
        for character_data in characters_data_list:
            user = random.choice(users)
            character = Character.objects.create(
                user=user,
                **character_data
            )
            self.stdout.write(self.style.SUCCESS(f'Character {character.name} created.'))
        
        self.stdout.write(self.style.SUCCESS('Successfully created characters.'))
        