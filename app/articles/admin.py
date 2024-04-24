from django.contrib import admin
from .models import Articles, Category, Tag, Comment

# Register your models here.
admin.site.register(Articles)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment)
