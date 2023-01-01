from django.contrib import admin
from .models import BlogPost


# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'created_on', 'last_updated',)
    list_editable = ('published',)
    ordering = ('-created_on',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(BlogPost, BlogPostAdmin)
