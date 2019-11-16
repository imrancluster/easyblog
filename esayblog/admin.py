from django.contrib import admin

from esayblog.models import BlogPost

# App customization for admin panel

class BlogPostAdmin(admin.ModelAdmin):

    # adding filter options using model fields
    list_filter = ['created_at']

    # adding search field
    search_fields = ['title', 'body']

admin.site.register(BlogPost, BlogPostAdmin)
