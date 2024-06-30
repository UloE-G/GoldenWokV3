from django.contrib import admin
from .models import Post, Comment

# Register your models here.

# Post model 
admin.site.register(Post)


# Comment model
admin.site.register(Comment)