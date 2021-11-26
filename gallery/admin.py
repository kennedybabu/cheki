from django.contrib import admin
from .models import User, Post, category

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ('category',)


admin.site.register(User)
admin.site.register(Post, PostAdmin)
admin.site.register(category)