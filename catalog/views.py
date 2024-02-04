from django.http import HttpResponse
from django.shortcuts import render
from catalog.models import Category, Product

# Create your views here.


def index(request):
    data_list = Category.objects.all()

    data = {
        'title': 'Магазин',
        'data_list': data_list
    }
    # return HttpResponse(data_list)
    return render(request, 'catalog/index.html', context=data)
