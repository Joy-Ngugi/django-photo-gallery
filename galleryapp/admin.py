from django.contrib import admin
from .models import Photo, Tag, Profile, Like, Subscriber


admin.site.register(Photo)
admin.site.register(Tag)
admin.site.register(Profile)
admin.site.register(Like)
admin.site.register(Subscriber)
