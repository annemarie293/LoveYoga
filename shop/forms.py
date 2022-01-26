from django import forms
from .models import ShopProducts


class ProductForm(forms.ModelForm):
    class Meta:
        model = ShopProducts
        fields = "__all__"

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'sku': 'Product SKU',
            'name': 'Product Name',
            'description': 'Product description',
            'price': 'Price',
            'category': 'Category'
            }
        image_label = "Upload image:"

        self.fields['name'].widget.attrs['autofocus'] = True
        print(self.fields.items())
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = "admin-input"
            if field_name != 'image':                
                placeholder = placeholders[field_name]
                self.fields[field_name].widget.attrs[
                        'placeholder'] = placeholder
                self.fields[field_name].label = False
            else:
                self.fields[field_name].label = image_label
            if field_name == 'category':
                self.fields[field_name].widget.attrs['class'] = "d-none"
                self.fields[field_name].widget.attrs['value'] = 'product'
