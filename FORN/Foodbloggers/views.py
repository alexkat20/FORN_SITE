from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import FVideo, FVideoComment


def index(request):
    all_videos = FVideo.objects.order_by('-pub_date')
    all_comments = FVideoComment.objects.order_by('comment_author')
    return render(request, 'homePage3.html', {'all_videos': all_videos, 'all_comments': all_comments})


def leave_comment(request, video_id):
    try:
        v = FVideo.objects.get(pk=video_id)
    except:
        raise Http404("Такого рецепта нет!")

    v.fvideocomment_set.create(comment_author=request.POST['name'], comment_text=request.POST['text'])
    return HttpResponseRedirect(reverse('Foodbloggers:index'))
