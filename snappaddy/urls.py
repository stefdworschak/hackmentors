from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('save/', save_image, name='save'),
]
