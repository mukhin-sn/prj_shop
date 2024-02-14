from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, contacts, ProductDetailView, ProductCategoryListView, ProductCreateView
from catalog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='index'),
    path('base/', contacts, name='contacts'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('category/<int:pk>/', ProductCategoryListView.as_view(), name='category'),
    path('create/', BlogCreateView.as_view(), name='create_blog'),
    path('blog/', BlogListView.as_view(), name='list_blog'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='detail_blog'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update_blog'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog'),

]
