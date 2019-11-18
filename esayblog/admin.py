from django.contrib import admin

from esayblog.models import BlogPost, Category


# admin.site.register(BlogPost, BlogPostAdmin)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):

    # adding filter options using model fields
    list_filter = ['created_at', 'category']

    # adding search field
    search_fields = ['title']

    # admin list display
    list_display = ['title', 'category']

    def get_search_results(self, request, queryset, search_term):
        qs, use_distinct = super().get_search_results(request, queryset, search_term)
        search_term = search_term.strip()
        if not search_term:
            return qs, use_distinct

        try:
            n = int(search_term)
            qs |= self.model.objects.filter(id__exact=n)
        except Exception as e:
            qs |= self.model.objects.filter(title__icontains=search_term)
            if not qs:
                qs |= self.model.objects.filter(body__icontains=search_term)

        return qs, use_distinct

@admin.register(Category)
class Category(admin.ModelAdmin):
    pass