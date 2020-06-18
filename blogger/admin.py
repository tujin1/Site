from django.contrib import admin
from .models import *



class PostAdmin(admin.ModelAdmin):
    pass



class BlogAdmin(admin.ModelAdmin):
    pass

#не успел доделать эту часть
admin.site.register(Blog, BlogAdmin)
admin.site.register(Post, PostAdmin)
