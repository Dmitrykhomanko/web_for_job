from django.shortcuts import render
from .models import Photo
def photos_main(request):
    photos = Photo.objects.all()
    context = {
        "title": "Фотки блюд",
        "photos": photos,
    }
    return render(request, "photos/photos_main.html", context)
