from django.contrib import admin

from esayblog.models import BlogPost, Category


# admin.site.register(BlogPost, BlogPostAdmin)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):

    # adding filter options using model fields
    list_filter = ['created_at']

    # adding search field
    search_fields = ['title', 'body']

@admin.register(Category)
class Category(admin.ModelAdmin):
    pass