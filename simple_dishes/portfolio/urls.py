from django.urls import path
from .views import resume, index, gallery_photos


urlpatterns = [
    # path('', index),
    path('', index, name='index'),
    path('resume/', resume, name='resume'),
    path('gallery_photos/', gallery_photos, name='gallery_photos'),



]
