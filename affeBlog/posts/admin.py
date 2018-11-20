from django.contrib import admin
# Register your models here.
from .models import Post


class IndexModelAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "timestamp", "updated"] # list_display is derived from ModelAdmin
    list_display_links = ["updated"]
    list_filter = ["updated"]
    search_fields = ["title", "content"]

    class Meta:
        model = Post

admin.site.register(Post, IndexModelAdmin)bbb