from django.core.management.base import BaseCommand

from feastinsight.models import Review
from feastinsight.ai_functions.openai_functions import add_theme_of_review

class Command(BaseCommand):
    help = "Add sentiment to all reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Force overwrite of existing sentiment'
        )

    def handle(self, *args, **options):
        reviews = Review.objects.all()
        force = options["force"]

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
