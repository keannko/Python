from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from shop.models import Phones


def main_page(request):
    phones = Phones.objects.all()
    return render(request, 'shop/main_page.html', {'phones': phones})

def index(request, p_id):
    return HttpResponse(f"{p_id}")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена </h1>')

