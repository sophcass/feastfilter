from django.core.management.base import BaseCommand

from feastinsight.models import Review
from feastinsight.ai_functions.openai_functions import add_sentiment_of_review

class Command(BaseCommand):
    help = "Add sentiment to all reviews"

    def handle(self, *args, **kwargs):
        reviews = Review.objects.all()

        for review in reviews.iterator():
            add_sentiment_of_review(review)

