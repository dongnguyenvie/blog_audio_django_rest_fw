from django.contrib import admin
from blogs.models import Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Blog, BlogAdmin)