import uuid

from django.conf import settings
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import JsonResponse

from .models import SnapPaddyImage


def index(request):
    """ Displays the canvas and lets user create a new image """
    return render(request, 'paddy_snap.html')


def test(request):
    """ Displays the canvas and lets user create a new image """
    return render(request, 'test.html')


def save_image(request):
    """ Converts image to base64 and saves it in the DB """
    # if not request.method == 'POST':
    #     return redirect(reverse('index'))

    snap = SnapPaddyImage(
        cutout=request.POST.get('cutout'),
        base64image=request.POST.get('snap-file')
    )
    snap.save()

    return redirect(f'/show/{snap.uuid}/')


def show_image(request, uuid_str):
    """ Displays the saved image and cutout """
    _uuid = uuid.UUID(uuid_str)
    snap = get_object_or_404(SnapPaddyImage, uuid=_uuid)
    return render(request, 'show_snap.html', {'snap': snap, 'host': settings.HOST})

