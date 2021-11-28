from django.contrib import admin
from .models import User, Post, category,location

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ('location',)

# class UserAdmin(admin.ModelAdmin):
#     filter_horizontal = ('location',)


admin.site.register(User)
admin.site.register(Post, PostAdmin)
admin.site.register(category)
admin.site.register(location)