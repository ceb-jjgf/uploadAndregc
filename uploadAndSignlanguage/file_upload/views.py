from django.shortcuts import render

from django.http import JsonResponse
from .forms import VideoForm


# Create your views here.
def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Video uploaded successfully!'}, status=200)
    else:
        form = VideoForm()
    return JsonResponse({'error': 'Invalid request'}, status=400)