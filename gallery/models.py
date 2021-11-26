from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    def save_user(self):
        self.save()

class category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Post(models.Model):
    # image =
    image_name = models.CharField(max_length=50)
    image_description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    category = models.ManyToManyField(category)
    pub_date = models.DateTimeField(auto_now_add=True)
