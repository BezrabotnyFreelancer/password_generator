from django.forms import ModelForm
from django.forms import TextInput, URLInput
from .models import PasswordStorage


class CreationPasswordInStorageForm(ModelForm):
    class Meta:
        model = PasswordStorage
        fields = ('site', 'password')
        widgets = {
            'site': URLInput(attrs={'class': 'form-control', 'placeholder': 'Your url'}),
            'password': TextInput(attrs={'class': 'form-control', 'placeholder': 'Your password'})
        }
        labels = {x: x.title() for x in fields}