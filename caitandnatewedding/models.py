from django.db import models

TITLES = [
    ('Mr.', 'Mr.'),
    ('Mrs.', 'Mrs.'),
    ('Ms.', 'Ms.'),
    ('Miss', 'Miss'),
    ('Dr.', 'Dr.'),
    ('Reverend Father', 'Reverend Father'),
]

STATES = [
    ('AL', 'AL'),
    ('AK', 'AK'),
    ('AZ', 'AZ'),
    ('AR', 'AR'),
    ('CA', 'CA'),
    ('CO', 'CO'),
    ('CT', 'CT'),
    ('DE', 'DE'),
    ('FL', 'FL'),
    ('GA', 'GA'),
    ('HI', 'HI'),
    ('ID', 'ID'),
    ('IL', 'IL'),
    ('IN', 'IN'),
    ('IA', 'IA'),
    ('KS', 'KS'),
    ('KY', 'KY'),
    ('LA', 'LA'),
    ('ME', 'ME'),
    ('MD', 'MD'),
    ('MA', 'MA'),
    ('MI', 'MI'),
    ('MN', 'MN'),
    ('MS', 'MS'),
    ('MO', 'MO'),
    ('MT', 'MT'),
    ('NE', 'NE'),
    ('NV', 'NV'),
    ('NH', 'NH'),
    ('NJ', 'NJ'),
    ('NM', 'NM'),
    ('NY', 'NY'),
    ('NC', 'NC'),
    ('ND', 'ND'),
    ('OH', 'OH'),
    ('OK', 'OK'),
    ('OR', 'OR'),
    ('PA', 'PA'),
    ('RI', 'RI'),
    ('SC', 'SC'),
    ('SD', 'SD'),
    ('TN', 'TN'),
    ('TX', 'TX'),
    ('UT', 'UT'),
    ('VT', 'VT'),
    ('VA', 'VA'),
    ('WA', 'WA'),
    ('WV', 'WV'),
    ('WI', 'WI'),
    ('WY', 'WY'),
]

COUNTRIES = [('US', 'US'), ('CA', 'CA')]


class Household(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2, choices=STATES)
    country = models.CharField(max_length=2, choices=COUNTRIES)
    zip_code = models.CharField(max_length=55)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    number_of_guests = models.PositiveIntegerField()
    rsvp_code = models.CharField(max_length=10)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Guest(models.Model):
    household = models.ForeignKey('Household', on_delete=models.CASCADE)
    title = models.CharField(max_length=55, choices=TITLES)
    first_name = models.CharField(max_length=55)
    middle_initial = models.CharField(max_length=10, null=True, blank=True)
    last_name = models.CharField(max_length=55)

    def __repr__(self):
        return self.title + ' ' + self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.title + ' ' + self.first_name + ' ' + self.last_name
