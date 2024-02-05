
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import index, contacts, product_page


app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product_page/', product_page, name='product_page'),

]