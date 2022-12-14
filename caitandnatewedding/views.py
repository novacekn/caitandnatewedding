from django.shortcuts import render
from django.http import JsonResponse

from .models import Household, Guest


def index(request):
    return render(request, 'index.html')


def rsvp(request):
    guest_ids = request.POST.getlist('guests[]')

    for guest_id in guest_ids:
        this_guest = Guest.objects.get(pk=int(guest_id))
        this_guest.is_attending = True
        this_guest.save()
    return JsonResponse({'message': '<h3>Guests successfully RSVPed!</h3>'}, safe=False)


def get_household_guests(request):
    name = request.POST.get('name').lower().split(' ')
    try:
        guest = Guest.objects.filter(first_name__contains=name[0], last_name__contains=name[1]).first()
    except Exception:
        return JsonResponse('<h3>No guest found with this name.</h3>', safe=False)
    guests = Guest.objects.filter(household=guest.household)
    i = 0
    html = '<label for="guests[]">Guests On Household (Please check all that are attending)</label>'
    for guest in guests:
        disabled = 'disabled checked' if guest.is_attending else ''
        html += f'''
        <div class="form-check">
            <input class="form-check-input" type="checkbox" name="guests[]" value="{guest.pk}" id="guest_{i}" {disabled}>
            <label class="form-check-label" for="guest_{i}">{guest.first_name} {guest.last_name}
        </div>
        '''
        i += 1
    html += '''
    <div class="col-md-12 text-center">
        <div class="form-group">
            <input type="button" id="guestSubmit" name="guestSubmit" class="button medium reverse" value="SUBMIT">
        </div>
    </div>
    '''
    return JsonResponse(html, safe=False)
