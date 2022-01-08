from django.contrib import admin

from short_link.models import Links


@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    list_display = ("id", "short_link", "full_link")
    list_display_links = ("short_link",)
