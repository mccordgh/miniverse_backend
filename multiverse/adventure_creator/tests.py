from django.test import TestCase
from django.test.utils import setup_test_environment
from django.contrib.auth.models import User
from adventure_creator import models

class AdventureModelTest(TestCase):

    def test_can_create_adventure_instance(self):
        user = User(
            username='mccordinator',
            password='pass1234',
            email='me@me.meep',
            first_name='Matty',
            last_name='McCordder'
        )
        adventure = models.Adventure(
            user=user,
            title='Awesome Adventure Dude'
        )
        self.assertIsInstance(adventure, models.Adventure)
        self.assertIsInstance(adventure.user, User)
        self.assertEqual(adventure.title, 'Awesome Adventure Dude')


class ExitModelTest(TestCase):

    def test_can_create_exit_instance(self):
        exit = models.Exit(
            direction='N'
        )
        self.assertIsInstance(exit, models.Exit)
        self.assertEqual(exit.direction, 'N')

class ItemModelTest(TestCase):

    def test_can_create_item_instance(self):
        item = models.Item(
            name='Hammer',
            description='Smash it up!'
        )
        self.assertIsInstance(item, models.Item)
        self.assertEqual(item.name, 'Hammer')
        self.assertEqual(item.description, 'Smash it up!')

class InteractiveModelTest(TestCase):

    def test_can_create_interactive_instance(self):
        item = models.Item(
            name='Hammer',
            description='Smash it up!'
        )
        interactive = models.Interactive(
            description='A glass vase with a crack in it',
            action='give',
            activator=item
        )
        self.assertIsInstance(interactive, models.Interactive)
        self.assertIsInstance(interactive.activator, models.Item)
        self.assertEqual(interactive.description, 'A glass vase with a crack in it')
        self.assertEqual(interactive.action, 'give')

class RoomModelTest(TestCase):

    def test_can_create_room_instance(self):
        user = User(
            username='mccordinator',
            password='pass1234',
            email='me@me.meep',
            first_name='Matty',
            last_name='McCordder'
        )
        adventure = models.Adventure(
            user=user,
            title='Awesome Adventure Dude'
        )
        item = models.Item(
            name='Hammer',
            description='Smash it up!'
        )
        interactive = models.Interactive(
            description='A glass vase with a crack in it',
            action='give',
            activator=item
        )
        room = models.Room(
            description='You enter a valley...',
            adventure=adventure,
            item=item,
            interactive=interactive
        )
        self.assertIsInstance(room, models.Room)
        self.assertIsInstance(interactive, models.Interactive)
        self.assertIsInstance(item, models.Item)
        self.assertIsInstance(adventure, models.Adventure)
        self.assertIsInstance(user, models.User)
        self.assertEqual(room.description, 'You enter a valley...')
