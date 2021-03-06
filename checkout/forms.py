from django import forms
from .models import Order


# Form to submit customer detials for orders
class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('full_name',
                  'email', 'phone_number', 'street_address1',
                  'street_address2', 'town_or_city',
                  'county', 'postcode', 'country',
                  )

    def __init__(self, *args, **kwargs):
        """
        Set placeholders to display, set autofocus on first field
        and clear any default labels
        """

        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email',
            'phone_number': 'Phone',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town/City',
            'county': 'County',
            'postcode': 'Post Code',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
