from django.contrib import admin

from feastinsight.models import Place, Review


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ["name", "formatted_address"]
    search_fields = ["name"]
    # TODO: Do we want to make some fields readonly?
    # readonly_fields = (
    #     "",
    # )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["place__name", "text"]
    search_fields = ["place__name"]
    # TODO: Do we want to make some fields readonly?
    # readonly_fields = (
    #     "",
    # )
