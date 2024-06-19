from django.shortcuts import render

from .models import Locations

# Create your views here.


def index(request):
    locations = Locations.objects.all()
    context = {'all_locations': locations}
    
    return render(request, 'conditions.html', context)

def detail(request, location_id):
    context = {
        "title": "Location_name",
    }
    return render(request, "condition/" % location_id, context)