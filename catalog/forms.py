from django import forms
from django.core.exceptions import ValidationError

from .config import VALID_WORDS
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        for field in self.fields.keys():
            self.fields.get(field).widget.attrs.update({
                'class': 'form-control',
                'placeholder': f'Введите {field}'
            })

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена должен быть больше нуля')
        return price

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        description = description.lower()
        name = name.lower()
        str_list = name.split()
        str_list.extend(description.split())
        print('str_list =>', str_list)
        for word in str_list:
            if word in VALID_WORDS:
                raise ValidationError(f'Имя или описание не должны содержать слово - {word}')
