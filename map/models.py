from django.db import models


class InstitutionType(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class TypeStreet(models.Model):
    STREET = 1
    AVENUE = 2
    BOULEVARD = 3
    HIGHWAY = 4

    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class City(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Institution(models.Model):
    YES_NO_CHOICES = (
        (False, 'Ні'),
        (True, 'Так')
    )

    institution_type = models.ForeignKey(InstitutionType, on_delete=models.SET_NULL, null=True, blank=True)
    name_object = models.CharField(max_length=255)
    special_parking_spaces = models.BooleanField(choices=YES_NO_CHOICES, default=False)
    input_group = models.BooleanField(choices=YES_NO_CHOICES, default=False)
    means_of_non_visual_orientation = models.BooleanField(choices=YES_NO_CHOICES, default=False)
    means_of_acoustic_orientation = models.BooleanField(choices=YES_NO_CHOICES, default=False)
    availability_of_special_elevator = models.BooleanField(choices=YES_NO_CHOICES, default=False)
    sanitary_and_hygienic_premises = models.BooleanField(choices=YES_NO_CHOICES, default=False)
    adapted_warning_devices = models.BooleanField(choices=YES_NO_CHOICES, default=False)
    sign_language_interpreter = models.BooleanField(choices=YES_NO_CHOICES, default=False)
    shelter = models.BooleanField(choices=YES_NO_CHOICES, default=False)
    wi_fi = models.BooleanField(choices=YES_NO_CHOICES, default=False)
    changing_table = models.BooleanField(choices=YES_NO_CHOICES, default=False)
    children_room = models.BooleanField(choices=YES_NO_CHOICES, default=False)
    accompanying_person = models.BooleanField(choices=YES_NO_CHOICES, default=False)
    phone_number = models.CharField(max_length=255, blank=True, default='')
    phone_call_center = models.CharField(max_length=255, blank=True, default='')
    distance_to_public_transport = models.IntegerField(blank=True, null=True)
    presence_of_tactile_route = models.BooleanField(choices=YES_NO_CHOICES, default=False)
    website_institution = models.CharField(max_length=255, blank=True, default='')
    institution_availability_page = models.CharField(max_length=255, blank=True, default='')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    type_street = models.ForeignKey(TypeStreet, on_delete=models.SET_NULL, null=True, blank=True)
    street_name = models.CharField(max_length=255, blank=True, default='')
    house_number = models.CharField(max_length=255, blank=True, default='')
    case_number = models.CharField(max_length=255, blank=True, default='')
    x_coord = models.FloatField()
    y_coord = models.FloatField()

    def __str__(self):
        return self.name_object
