from django.forms import ModelForm
from tinymce.widgets import TinyMCE
from django import forms


from .models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ('name', 'topic', 'location', 'date', 'time', 'price', 'description')
        labels = {
            'description': "",
            'topic': "",
            'name': "",
            'price': "",
            'date': "",
            'time': "",
            'location': "",
        }
        widgets = {
            'topic': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Dla dzieci'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Koncert Ich Troje'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'HH:MM'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Las Zwierzyniecki'}),
            'description': TinyMCE(attrs={"cols": 80, "rows": 30, "class": "form-control"})
        }
        # description = forms.CharField(widget=TinyMCE(attrs={"cols": 80, "rows": 30, "class": "form-control"}))
        # date = forms.DateField(widget=DatePickerInput(options={"format": "mm/dd/yyyy", "autoclose": True}))
