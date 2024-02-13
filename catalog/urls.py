from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, contacts, ProductListView, ProductCategoryListView
from catalog.views import BlogListView, BlogDetailView  # BlogDeleteView, BlogCreateView, BlogUpdateView,

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='index'),
    path('base/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductListView.as_view(), name='product'),
    path('category/<int:pk>/', ProductCategoryListView.as_view(), name='category'),
    # path('blog/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/', BlogDetailView.as_view(), name='blog_detail'),
    # path('blog/', BlogUpdateView.as_view(), name='blog_update'),
    # path('blog/', BlogDeleteView.as_view(), name='blog_delete'),

]
