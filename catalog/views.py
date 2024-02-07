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
    for dl in data['data_list']:
        if len(dl.description) > 100:
            dl.description = dl.description[:100]
        # else:
        #     string_of_spaces = " " * (100 - len(dl.description))
        #     dl.description = dl.description + string_of_spaces
        # print(len(dl.description), dl.description)

    # return HttpResponse(data_list)
    return render(request, 'catalog/index.html', context=data)


def contacts(request):
    data = {
        'title': 'Контактная информация',
        'data': False
    }

    if request.method == 'POST':
        data['name'] = request.POST.get('name')
        data['phone'] = request.POST.get('phone')
        data['message'] = request.POST.get('message')
        data['data'] = True

        print(f'{data["name"]}, {data["phone"]}\n{data["message"]}')
    return render(request, 'catalog/contacts.html', context=data)


def product(request, pk):

    data_list = Product.objects.filter(pk=pk)
    data = {
        'title': 'Продукт',
        'data_list': data_list,
    }

    for dl in data['data_list']:
        if len(dl.description) > 100:
            dl.description = dl.description[:100]
        # print(len(dl.description), dl.description)

    return render(request, 'catalog/product_page.html', context=data)


def category(request, pk):

    data_list = Product.objects.filter(category_id=pk)
    data = {
        'title': 'Категории товаров',
        'data_list': data_list,
        'category_id': pk,
    }
    # for i in data['data_list']:
    #     print(i.image)

    return render(request, 'catalog/category_page.html', context=data)
