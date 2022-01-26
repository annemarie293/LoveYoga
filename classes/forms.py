from django import forms
from .models import YogaClass


class ClassForm(forms.ModelForm):
    class Meta:
        model = YogaClass
        fields = "__all__"

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields:
                field.widget.attrs['class'] = "admin-input"
