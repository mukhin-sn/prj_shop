from django.contrib import admin

from catalog.models import Category, Product, Blog, Version


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    # list_filter = ('',)
    # search_fields = ('',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price_for_one', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'views_count',)
    list_filter = ('is_published', 'views_count',)
    search_fields = ('name', 'content', 'creation_date',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'version_number', 'version_name', 'current_version_indicator',)
    list_filter = ('product', 'version_number', 'version_name',)
    search_fields = ('product', 'version_number', 'version_name', 'current_version_indicator',)
