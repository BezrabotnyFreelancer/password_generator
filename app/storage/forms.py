from django import forms


class CreationPasswordInStorageForm(forms.Form):
    site = forms.URLField(label='Site URL', help_text='Input an url address',
                          widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Your url'}))
    
    password = forms.CharField(label='Password', help_text='Input a password of site',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your password'}))
