import logging
from django.core.management.base import BaseCommand

from feastinsight.places import get_places_data

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Get Places data from Google API"

    def handle(self, *args, **options):
        logger.info("Get Places data from API")
        get_places_data()
