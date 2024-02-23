from django import forms

from catalog.models import Product, Version
from config.settings import PROHIBITED_COMBINATIONS


class FormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'current_version_indicator':
                field.widget.attrs['class'] = 'form-control'


class ProductForm(FormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ('name', 'category',)
        # exclude = ('image',)

    def word_check(self, var: str, *args, **kwargs) -> bool:
        """
        Метод формирования списка слов из вводимого предложения
        и его валидации.
        Слитно написанные несколько запрещенных слов (без разделяющих символов)
        валидацию пройдут.
        Возвращает True, если валидация прошла успешно.
        """
        alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        data_str = self.cleaned_data.get(var)
        out_list = []

        # сделаем список из строки
        data_list = data_str.lower().split(' ')

        # уберем все лишние символы из слов
        for word in data_list:
            var_word = ''
            for letter in word:
                if letter in alphabet:
                    var_word += letter
                else:
                    out_list.append(var_word)
                    var_word = ''
            out_list.append(var_word)

        for word in out_list:
            if word in args:
                raise forms.ValidationError('Присутствуют запрещенные слова')
        return True

    def clean_name(self):
        """
        clean-метод для поля name продукта
        """
        if self.word_check('name', *PROHIBITED_COMBINATIONS):
            return self.cleaned_data.get('name')

    def clean_description(self):
        """
        clean-метод для поля description продукта
        """
        if self.word_check('description', *PROHIBITED_COMBINATIONS):
            return self.cleaned_data.get('description')


class VersionForm(FormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    # def clean_current_version_indicator(self):
    #     product_id = self.cleaned_data.get('product')
    #     version_list = Version.objects.filter(product_id=product_id)
    #     activation_counter = 0
    #     for cvi in version_list:
    #         if cvi.current_version_indicator:
    #             activation_counter += 1
    #     if activation_counter > 1:
    #         print('Активна может быть только одна версия')
    #         for cvi in version_list:
    #             cvi.current_version_indicator = False
    #             print('Сброс')
    #         # raise forms.ValidationError(False)
    #     # return self.cleaned_data.get('current_version_indicator')
    #     return None
