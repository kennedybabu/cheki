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

    # def test_delete_method(self, id):
    #     if self.id == id:
    #         self.delete_user()
    #         users = User.objects.all()
    #         self.assertTrue(len(users) == 0)

class PostTestClass(TestCase):
    def setUp(self):
        self.jude = User(first_name='jude', last_name='babu', email='jude@moringa.com')
        self.jude.save_user()

        self.new_category = category(name='testing')
        self.new_category.save()

        self.new_post = Post()
        self.new_post.save()

        self.new_post.category.add(self.new_category)

    def tearDown(self):
        User.objects.all().delete()
        Post.objects.all().delete()
        category.objects.all().delete()

    def test_get_posts(self):
        all_posts = Post.all_posts()
        self.assertTrue(len(all_posts) > 0)
