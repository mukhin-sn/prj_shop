from django.db import models

# Create your models here.

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=200, verbose_name='описание')
    # created_at = models.DateField(verbose_name='дата создания', **NULLABLE)

    def __str__(self):
        return f'{self.name} '

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=200, verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, max_length=50, verbose_name='категория')
    price_for_one = models.IntegerField(verbose_name='цена за штуку')
    date_of_creation = models.DateField(verbose_name='дата создания', **NULLABLE)
    last_modified_date = models.DateField(verbose_name='дата последнего изменения', **NULLABLE)

    def __str__(self):
        return f'{self.name} '

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Blog(models.Model):
    name = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='preview/', verbose_name='превью', **NULLABLE)
    creation_date = models.DateField(verbose_name='дата создания', **NULLABLE)
    is_published = models.BooleanField(verbose_name='опубликовано', default=True)
    views_count = models.IntegerField(verbose_name='количество просмотров', default=0)

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'

    def __str__(self):
        return f'{self.title}'

