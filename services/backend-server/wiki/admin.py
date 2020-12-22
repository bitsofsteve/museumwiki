from django.contrib import admin

from .models import Wiki


@admin.register(Wiki)
class WikiAdmin(admin.ModelAdmin):
    fields = (
        "name",
        "established",
        "city",
        "country",
        "collection_size",
        "visitors",
        "website",
        "created_date",
        "updated_date",
    )

    list_display = (
        "name",
        "established",
        "city",
        "country",
        "collection_size",
        "visitors",
        "website",
        "created_date",
        "updated_date",
    )

    readonly_fields = ("created_date", "updated_date")
