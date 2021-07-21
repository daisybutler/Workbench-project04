from django.shortcuts import render
from .models import Locations
import json


def locations(request):

    """A view to render the locations page"""

    locations = Locations.objects.all()

    coords = {}
    for location in locations:
        name = location.location
        value = {
            "lat": location.lat,
            "lng": location.lng,
        }

        coords[name] = value

    context = {
        'locations': locations,
        'coords': json.dumps(coords),
    }

    return render(request, 'locations/locations.html', context)
