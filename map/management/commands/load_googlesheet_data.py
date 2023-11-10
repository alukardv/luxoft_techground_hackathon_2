import csv

from django.core.management.base import BaseCommand

from map.models import InstitutionType, TypeStreet, City, Institution


class Command(BaseCommand):
    help = 'Імпорт даних закладів з файлу'

    @classmethod
    def int_safe(cls, arg):
        try:
            return int(arg)
        except ValueError:
            return None

    def add_arguments(self, parser):
        parser.add_argument('file', type=str, help='Шлях до файлу для імпорту')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['file']

        all_institution_types = InstitutionType.objects.all()
        all_street_types = TypeStreet.objects.all()
        all_cities = City.objects.all()

        try:
            with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)
                header = next(csv_reader, None)

                for idx, row in enumerate(csv_reader, 1):
                    institution_type = all_institution_types.filter(title__iexact=row[1].strip()).first()
                    city = all_cities.filter(title__iexact=row[22].strip()).first()
                    type_street = all_street_types.filter(title__iexact=row[23].strip()).first()

                    Institution.objects.create(
                        institution_type=institution_type or None,
                        name_object=row[2].strip(),
                        special_parking_spaces=True if row[3].strip().lower() == 'так' else False,
                        input_group=True if row[4].strip().lower() == 'так' else False,
                        means_of_non_visual_orientation=True if row[5].strip().lower() == 'так' else False,
                        means_of_acoustic_orientation=True if row[6].strip().lower() == 'так' else False,
                        availability_of_special_elevator=True if row[7].strip().lower() == 'так' else False,
                        sanitary_and_hygienic_premises=True if row[8].strip().lower() == 'так' else False,
                        adapted_warning_devices=True if row[9].strip().lower() == 'так' else False,
                        sign_language_interpreter=True if row[10].strip().lower() == 'так' else False,
                        shelter=True if row[11].strip().lower() == 'так' else False,
                        wi_fi=True if row[12].strip().lower() == 'так' else False,
                        changing_table=True if row[13].strip().lower() == 'так' else False,
                        children_room=True if row[14].strip().lower() == 'так' else False,
                        accompanying_person=True if row[15].strip().lower() == 'так' else False,
                        phone_number=row[16].strip(),
                        phone_call_center=row[17].strip(),
                        distance_to_public_transport=self.int_safe(row[18].strip()),
                        presence_of_tactile_route=True if row[19].strip().lower() == 'так' else False,
                        website_institution=row[20].strip(),
                        institution_availability_page=row[21].strip(),
                        city=city or None,
                        type_street=type_street or None,
                        street_name=row[24].strip(),
                        house_number=row[25].strip(),
                        case_number=row[26].strip(),
                        x_coord=float(row[27].strip()),
                        y_coord=float(row[28].strip()),
                    )
                    print(f'{idx:>3}. Успішно імпортовано')

        except FileNotFoundError:
            print(f'Файл {csv_file_path} не знайдено')
