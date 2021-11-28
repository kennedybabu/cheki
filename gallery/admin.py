from django.contrib import admin
from .models import User, Post, Category,location

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ('location','category')

# class UserAdmin(admin.ModelAdmin):
#     filter_horizontal = ('location',)


admin.site.register(User)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(location)