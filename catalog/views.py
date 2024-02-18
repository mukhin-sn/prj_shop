from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from catalog.forms import ProductForm
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


class ProductDetailView(DetailView):
    model = Product
    extra_context = {
        'title': 'Продукт'
    }

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(pk=self.kwargs.get('pk'))
    #     return queryset


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
#     return render(request, 'catalog/product_details.html', context=data)


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


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self, *args, **kwargs):
        return reverse('catalog:category', args=[self.object.category_id])


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

class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Продукты'
    }


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self, *args, **kwargs):
        return reverse('catalog:category', args=[self.object.category_id])


class ProductDeleteView(DeleteView):
    model = Product

    def get_success_url(self, *args, **kwargs):
        return reverse('catalog:category', args=[self.object.category_id])


class BlogCreateView(CreateView):
    model = Blog
    fields = '__all__'
    success_url = reverse_lazy('catalog:list_blog')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.name)
            new_blog.save()
        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog
    extra_context = {
        'title': 'Блоги',
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('name', 'content', 'image', 'creation_date', 'is_published')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.name)
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:detail_blog', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:list_blog')
