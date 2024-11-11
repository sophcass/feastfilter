from django.core.management.base import BaseCommand, CommandError

from feastinsight.models import Place
from feastinsight.ai_functions import openai_functions, anthropic_functions

class Command(BaseCommand):
    help = "Add enhanced name to all restaurants"

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Force overwrite of existing enhanced name'
        )
        parser.add_argument(
            "--open-ai",
            action="store_true",
            help="Use OpenAI function to get the enhanced name"
        )
        parser.add_argument(
            "--claude",
            action="store_true",
            help="Use Claude function to get the enhanced name"
        )

    def handle(self, *args, **options):
        restaurants = Place.objects.all()
        force = options["force"]

        if options["open_ai"] and options["claude"]:
            raise CommandError("Cannot specify both --open-ai and --claude. Choose one.")
        elif not options["open_ai"] and not options["claude"]:
            raise CommandError("You must specify either --open-ai or --claude.")

        if options["open_ai"]:
            add_enhanced_name = openai_functions.add_enhanced_name
        else:
            add_enhanced_name = anthropic_functions.add_enhanced_name

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
