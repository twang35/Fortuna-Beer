from django import forms

class NameForm(forms.Form):
    searchBeer = forms.CharField(label='Your name', max_length=100)