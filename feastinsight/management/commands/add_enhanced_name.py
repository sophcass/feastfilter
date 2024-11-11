from django.core.management.base import BaseCommand

from feastinsight.models import Place
from feastinsight.ai_functions.openai_functions import add_enhanced_name

class Command(BaseCommand):
    help = "Add enhanced name to all restaurants"

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Force overwrite of existing enhanced name'
        )

    def handle(self, *args, **options):
        restaurants = Place.objects.all()
        force = options["force"]

        for restaurant in restaurants.iterator():
            if not restaurant.enhanced_name or force:
                add_enhanced_name(restaurant)
            else:
                print(
                    f"Already populated enhanced_name for restaurant {restaurant.id}\n"
                    "Use --force if you want to overwrite."
                )

        DJANGO_ADMIN_URL = "http://127.0.0.1:8000/admin/feastinsight/place/"
        print(f"Finished writing enhanced name! Please visit {DJANGO_ADMIN_URL} to view results.")
