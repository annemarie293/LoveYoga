from django import forms
from .models import YogaClass, Practice
from trainers.models import Trainer


class ClassForm(forms.ModelForm):
    class Meta:
        model = YogaClass
        fields = "__all__"

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'sku': 'Class SKU',
            'name': 'Class Name',
            'description': 'Class description',
            'price': 'Price',
            'category': 'Category',
            'practice': 'Yoga Practice',
            'level': 'Difficulty Level',
            'intensity': 'Class Intensity',
            'session_duration': 'Session duration (minutes)',
            'series_duration': 'No. of sessions',
            'equipment': 'Equipment',
            'trainer': 'Trainer',
            }

        image_label = "Upload image:"

        # Gets the trainer name label from Trainer model
        trainers = Trainer.objects.all()
        trainer_names = [(c.id, c.get_label_name()) for c in trainers]
        self.fields['trainer'].choices = trainer_names

        # Gets the practice name label from Practice model
        practices = Practice.objects.all()
        practice_names = [(c.id, c.get_label_name()) for c in practices]
        self.fields['practice'].choices = practice_names

        # Sets autofocus to name field
        self.fields['name'].widget.attrs['autofocus'] = True

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = "admin-input"
            if field_name != 'image':                
                placeholder = placeholders[field_name]
                self.fields[field_name].widget.attrs[
                        'placeholder'] = placeholder
                self.fields[field_name].label = False
            else:
                self.fields[field_name].label = image_label
            # Hides category field and sets value as "class"
            if field_name == 'category':
                self.fields[field_name].widget.attrs['class'] = "d-none"
                self.fields[field_name].widget.attrs['value'] = 'class'

