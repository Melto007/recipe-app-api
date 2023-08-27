"""
Django command to wait for the database to be available.
"""
from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as psycopg2Error
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        """Entry Point for commands."""
        self.stdout.write('Waiting for database....')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (psycopg2Error, OperationalError):
                self.stdout.write('DB is not connected')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("DB is connected"))
