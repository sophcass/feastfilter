from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Populate insight of the restaurant using GenAI"

    def handle(self, *args, **kwargs):
        pass