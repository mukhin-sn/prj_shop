from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, contacts, ProductDetailView, ProductCategoryListView


app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='index'),
    path('base/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('category/<int:pk>/', ProductCategoryListView.as_view(), name='category'),
]
