
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductDetailView, ProductCategoryListView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('category/<int:pk>/', ProductCategoryListView.as_view(), name='category'),

]