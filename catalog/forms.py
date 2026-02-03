from django import forms
from django.core.exceptions import ValidationError

from .models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name_product', 'description_product', 'category_product', 'price_product', 'publication_status', 'owner']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name_product'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название продукта'
        })
        self.fields['description_product'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание продукта'
        })
        self.fields['category_product'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите категорию продукта'
        })
        self.fields['price_product'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену продукта'
        })

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name_product')
        description = cleaned_data.get('description_product')
        spam_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in spam_words:
            if word in name.lower():
                self.add_error('name_product', 'название или описание содержит запрещённые слова')
            if word in description.lower():
                self.add_error('description_product', 'название или описание содержит запрещённые слова')
        #if 'казино' or 'криптовалюта' or'крипта' or 'биржа' or 'дешево' or 'бесплатно' or 'обман' or 'полиция' or 'радар' in name or description:
            #self.add_error('name_product','название или описание содержит запрещённые слова')
            #self.add_error('description_product', 'название или описание содержит запрещённые слова'

    def clean_price_product(self):
        price = self.cleaned_data.get('price_product')
        if int(price) <= 0:
            raise ValidationError('цене не может быть равна или меньше 0')
        return price

