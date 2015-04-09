from django import forms

class NameForm(forms.Form):
    searchBeer = forms.CharField(label='', max_length=100, required=False, widget=forms.widgets.TextInput(attrs={'class': 'form-search', 'placeholder': 'Search Beers'}))