from django import forms

class NameForm(forms.Form):
    searchBeer = forms.CharField(label='searchBeer', max_length=100)