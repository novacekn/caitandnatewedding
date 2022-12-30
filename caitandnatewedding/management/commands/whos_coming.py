import csv
from django.core.management.base import BaseCommand
from caitandnatewedding.models import Guest


class Command(BaseCommand):
    help = 'A tool for seeing who has RSVPed and who has not'

    def handle(self, *args, **options):
        coming = Guest.objects.filter(is_attending=True)
        coming = [[str(o)] for o in coming]

        not_coming = Guest.objects.filter(is_attending=False)
        not_coming = [[str(o)] for o in not_coming]

        no_response = Guest.objects.filter(is_attending=None)
        no_response = [[str(o)] for o in no_response]

        with open('coming.csv', 'w') as coming_f:
            writer = csv.writer(coming_f)
            writer.writerows(coming)

        with open('not_coming.csv', 'w') as not_coming_f:
            writer = csv.writer(not_coming_f)
            writer.writerows(not_coming)

        with open('no_response.csv', 'w') as no_response_f:
            writer = csv.writer(no_response_f)
            writer.writerows(no_response)
