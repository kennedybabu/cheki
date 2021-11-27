from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    # posts = models.ManyToManyField(post)

    def __str__(self):
        return self.first_name

    def save_user(self):
        self.save()

    def delete_user(self, id):
        if self.id == id:
            self.delete()

class category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class location(models.Model):
    name = models.CharField(max_length=30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self, new):
        self.name = new.name
        self.save()

    def __str__(self):
        return self.name

class Post(models.Model):
    # image =
    image_name = models.CharField(max_length=50)
    image_description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    category = models.ManyToManyField(category)
    location = models.ManyToManyField(location)
    pub_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def all_posts(cls):
        posts = cls.objects.all()
        return posts

    @classmethod
    def search_by_title(cls, search_term):
        posts = cls.objects.filter(image_name__icontains=search_term)
        return posts
