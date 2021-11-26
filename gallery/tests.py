from django.test import TestCase
from .models import User, Post, category

# Create your tests here.

class UserTest(TestCase):
    #set up method
    def setUp(self):
        self.jude = User(first_name='jude', last_name='babu', email='jude@moringa.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.jude, User))

    def test_save_method(self):
        self.jude.save_user()
        users = User.objects.all()
        self.assertTrue(len(users) > 0)
