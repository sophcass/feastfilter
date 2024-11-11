from django.core.management.base import BaseCommand, CommandError

from feastinsight.models import Review
from feastinsight.ai_functions import openai_functions, anthropic_functions

class Command(BaseCommand):
    help = "Add sentiment to all reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Force overwrite of existing sentiment'
        )
        parser.add_argument(
            "--open-ai",
            action="store_true",
            help="Use OpenAI function to get the enhanced name"
        )
        parser.add_argument(
            "--anthropic",
            action="store_true",
            help="Use Anthropic function to get the enhanced name"
        )

    def handle(self, *args, **options):
        reviews = Review.objects.all()
        force = options["force"]

        if options["open_ai"] and options["anthropic"]:
            raise CommandError("Cannot specify both --open-ai and --anthropic. Choose one.")
        elif not options["open_ai"] and not options["anthropic"]:
            raise CommandError("You must specify either --open-ai or --anthropic.")

        if options["open_ai"]:
            add_theme_of_review = openai_functions.add_theme_of_review
        else:
            add_theme_of_review = anthropic_functions.add_theme_of_review

        for review in reviews.iterator():
            if not review.theme or force:
                add_theme_of_review(review)
            else:
                print(
                    f"Already populated theme of review {review.id}\n"
                    "Use --force if you want to overwrite."
                )

        DJANGO_ADMIN_URL = "http://127.0.0.1:8000/admin/feastinsight/review/"
        print(f"Finished tagging theme! Please visit {DJANGO_ADMIN_URL} to view results.")
