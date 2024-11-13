from django.contrib import admin

from feastinsight.models import Place, Review


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ["name", "formatted_address", "openai_enhanced_name", "anthropic_enhanced_name"]
    search_fields = ["name"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["place__name", "text", "openai_sentiment", "anthropic_sentiment"]
    search_fields = ["place__name"]
