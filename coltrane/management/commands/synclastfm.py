import logging
logger = logging.getLogger(__name__)
from django.conf import settings
from coltrane.utils import lastfm
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Sync Last.fm tracks'

    def handle(self, *args, **options):
        logger.debug("Syncing Last.fm data")
        client = lastfm.LastFMClient(
            settings.LASTFM_USER,
            settings.LASTFM_TAG_USAGE_THRESHOLD
        )
        client.sync()
