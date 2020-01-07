from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from .models import Menu


def index(request):
    all_menu = Menu.objects.all
    return render(request, 'homePage4.html', {'all_menu': all_menu})


def choose_menu(request, menu_id):
    try:
        m = Menu.objects.get(pk=menu_id)

    except:
        raise Http404("Такого рецепта нет!")

    request.user.profile.menu = m
    request.user.save()
    return HttpResponseRedirect(reverse('Menu:index'))


def see_menu(request, menu_id):
    try:
        m = Menu.objects.get(id=menu_id)
    except:
        raise Http404("Такого рецепта нет!")

    return render(request, 'detail_menu.html', {'Menu': m})
