from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse

from .models import SnapPaddyImage


def index(request):
    """ Displays the canvas and lets user create a new image """
    return render(request, 'index.html')


def save_image(request):
    """ Converts image to base64 and saves it in the DB """
    # if not request.method == 'POST':
    #     return redirect(reverse('index'))

    snap = SnapPaddyImage(
        cutout=request.POST.get('cutout'),
        base64image=request.POST.get('snap-file')
    )
    snap.save()

    return JsonResponse({'ok': True, 'uuid': snap.uuid})
    