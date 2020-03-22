from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home_view(request, *args, **kwdargs):
    # return HttpResponse("<h1>This is my website using django</h1>")
    return render(request, "home.html", {})


def contact_view(request, *args, **kwdargs):
    my_context = {
        "my_value": "wow love it",
        "my_digit": 10
    }

    return render(request, "contact.html", my_context)
