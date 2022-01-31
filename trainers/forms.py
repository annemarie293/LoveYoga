from django import forms
from .models import Trainer


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
             'name': 'First Name',
             'years_practicing': 'Number of years practicing Yoga',
             'years_teaching': 'Number of years teaching Yoga',
             'bio': 'Personal bio'
             }
        image_label = "Upload image:"

        self.fields['name'].widget.attrs['autofocus'] = True
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = "admin-input"
            if field_name != 'image':            
                placeholder = placeholders[field_name]
                self.fields[
                     field_name].widget.attrs['placeholder'] = placeholder
                self.fields[field_name].label = False
            else:
                self.fields[field_name].label = image_label
