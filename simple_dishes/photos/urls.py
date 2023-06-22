from django.urls import path
from .views import photos_main


urlpatterns = [

    path('', photos_main, name='photos_main'),

]
