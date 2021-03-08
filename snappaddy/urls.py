from django.urls import path, re_path

from .views import *

urlpatterns = [
    re_path('^$', index, name='index'),
    path('show/<str:uuid_str>/', show_image, name="show"),
    path('save/', save_image, name='save'),
    path('test/',test, name='test'),
]
