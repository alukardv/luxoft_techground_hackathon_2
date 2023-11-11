import csv

from django.core.management.base import BaseCommand

from map.models import ObjectOnMap


class Command(BaseCommand):
    help = 'Load data from CSV into Django model'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        file_path = options['file_path']
        with open(file_path, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                ObjectOnMap.objects.create(
                    name_object=row['name_object'].strip(),
                    type_object=row['type_object'].strip(),
                    x_coord=float(row['x_coord'].strip()),
                    y_coord=float(row['y_coord'].strip())
                )
