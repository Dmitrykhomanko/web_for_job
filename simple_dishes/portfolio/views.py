from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'portfolio/index.html', {'title':'Simple Dishes = ГЛАВНАЯ СТРАНИЦА'})


def resume(request):
    return render(request, 'portfolio/resume.html', {'title':'Мое резюме'})


def gallery_photos(request):
    return render(request, 'portfolio/gallery_photos.html')
# шаблонизатор render  его надо партировать евли его нет а HttpResponse  - созда одну страницу и на ней навдрр писать весь скилет html dcnfdkznm тоже партирует

