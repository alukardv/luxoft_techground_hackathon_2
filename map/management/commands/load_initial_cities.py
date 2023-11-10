from django.core.management.base import BaseCommand

from map.models import City


class Command(BaseCommand):
    help = 'Імпорт міст з файлу'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str, help='Шлях до файлу для імпорту')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file']

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                city, idx = file.readline().rstrip(), 1

                while city:
                    City.objects.create(title=city)
                    print(f'{idx:>4}. Успішно імпортовано [{city}]')

                    city = file.readline().rstrip()
                    idx += 1

        except FileNotFoundError:
            print(f'Файл {file_path} не знайдено')
