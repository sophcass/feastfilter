from django.core.management.base import BaseCommand

from feastinsight.ai_functions.openai import add_sentiment_of_review

class Command(BaseCommand):
    help = "Populate insight of the restaurant using GenAI"

    def handle(self, *args, **kwargs):
        add_sentiment_of_review()