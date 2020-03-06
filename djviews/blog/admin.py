from django.contrib import admin
from .models import PostModel

# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'slug',
        'content',
        'publish',
        'publish_date',
        'active'
    ]
    readonly_fields = ['updated', 'timestamp']

    class Meta:
        model = PostModel

admin.site.register(PostModel, PostModelAdmin)