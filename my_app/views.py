from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import EnteredQueries
from .running_line_sсript import create_running_line_video


# Create your views here.
def index(request):
    return render(request, 'my_app/index.html')


def download(request):
    if request.method == 'POST':
        if request.POST['text'] == 0:
            return render(request, 'my_app/index.html')

        new_query = EnteredQueries( entered_text=request.POST['text'])
        new_query.save()

        titel = create_running_line_video(request.POST['text'],
                                          request.POST['textcolor'],
                                          request.POST['backgroundcolor'])
        video_name = f"{titel}.mp4"
        vid_path = f'my_app/media/{video_name}'
        with open(vid_path, 'rb') as video_file:
            response = HttpResponse(video_file, content_type='video/avi')
            response['Content-Disposition'] = f'attachment; filename="{video_name}"'
            return response
    return render(request, 'my_app/index.html')