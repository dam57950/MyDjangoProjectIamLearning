from django.shortcuts import render

from .models import PhotoElement


# Create your views here.

def photo_detail_view(request, *args, **kwdargs):
    obj = PhotoElement.objects.get(id=3)
    #    context = {
    #        'titre': obj.name,
    #        'lieu': obj.place,
    #        'description': obj.description
    #    }

    context = {
        'object': obj
    }
    return render(request, "product/details.html", context)

# def photos_presentation_view(request, *args, **kwargs):
