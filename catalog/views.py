from django.shortcuts import render
from catalog.models import Product, Category, Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/index.html'
    extra_context = {
        'title': 'Магазин'
    }

# def index(request):
#     object_list = Category.objects.all()
#
#     data = {
#         'title': 'Магазин',
#         'object_list': object_list
#     }
#     for dl in data['object_list']:
#         if len(dl.description) > 100:
#             dl.description = dl.description[:100]
#         # else:
#         #     string_of_spaces = " " * (100 - len(dl.description))
#         #     dl.description = dl.description + string_of_spaces
#         # print(len(dl.description), dl.description)
#
#     # return HttpResponse(data_list)
#     return render(request, 'catalog/index.html', context=data)


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
    return render(request, 'catalog/base.html', context=data)


class ProductListView(ListView):
    model = Product
    # template_name = 'catalog/product_page.html'
    extra_context = {
        'title': 'Продукт'
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get('pk'))
        return queryset


# def product(request, pk):
#
#     object_list = Product.objects.filter(pk=pk)
#     data = {
#         'title': 'Продукт',
#         'object_list': object_list,
#     }
#
#     for dl in data['object_list']:
#         if len(dl.description) > 100:
#             dl.description = dl.description[:100]
#         # print(len(dl.description), dl.description)
#
#     return render(request, 'catalog/product_page.html', context=data)


class ProductCategoryListView(ListView):
    model = Product
    template_name = 'catalog/category_list.html'
    extra_context = {
        'title': 'Категории товаров',
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        self.extra_context['category_id'] = self.kwargs.get('pk')
        # print(self.extra_context['category_id'])
        return queryset


# def category(request, pk):
#
#     object_list = Product.objects.filter(category_id=pk)
#     data = {
#         'title': 'Категории товаров',
#         'object_list': object_list,
#         'category_id': pk,
#     }
#     # for i in data['object_list']:
#     #     print(i.image)
#
#     return render(request, 'catalog/category_page.html', context=data)


# class BlogCreateView(CreateView):
#     model = Blog


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog


# class BlogUpdateView(UpdateView):
#     model = Blog


# class BlogDeleteView(DeleteView):
#     model = Blog
