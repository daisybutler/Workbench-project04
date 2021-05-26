from django.shortcuts import render, get_object_or_404
from .models import Locations


def locations(request):

    locations = Locations.objects.all()

    context = {
        'locations': locations,
    }

    return render(request, 'locations/locations.html', context)
