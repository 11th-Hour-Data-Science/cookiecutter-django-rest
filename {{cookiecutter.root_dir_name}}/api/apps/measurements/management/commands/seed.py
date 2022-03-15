"""
Custom management command. Running python manage.py <filename> <args>
will run the Command.handle() method defined in this file. 
Reference: https://docs.djangoproject.com/en/4.0/howto/custom-management-commands/
"""

from django.core.management.base import BaseCommand, CommandError
from apps.measurements.factories import StationWithMeasurementFactory

class Command(BaseCommand):
    help = "Generates fake database entries for quick testing"

    def add_arguments(self, parser):
        parser.add_argument('num_stations', type=int)

    def handle(self, *args, **options):
        for n in options["num_stations"]:
            new_station = StationWithMeasurementFactory.create()