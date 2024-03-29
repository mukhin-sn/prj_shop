from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import *

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='index'),
    path('base/', contacts, name='contacts'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('product_update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product_delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('category/<int:pk>/', ProductCategoryListView.as_view(), name='category'),
    path('create/', BlogCreateView.as_view(), name='create_blog'),
    path('blog/', BlogListView.as_view(), name='list_blog'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='detail_blog'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update_blog'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog'),
    path('version_list/', VersionListView.as_view(), name='list_version'),
    path('version_create/', VersionCreateView.as_view(), name='create_version'),
    path('version_detail/<int:pk>/', VersionDetailView.as_view(), name='detail_version'),
    path('version_update/<int:pk>/', VersionUpdateView.as_view(), name='update_version'),
    path('version_delete/<int:pk>/', VersionDeleteView.as_view(), name='delete_version'),

]
