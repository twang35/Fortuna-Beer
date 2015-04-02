from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from randBeer.models import Beer

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Confirmation'}))
 
    def is_valid(self):
        form = super(UserCreateForm, self).is_valid()
        for f, error in self.errors.iteritems():
            if f != '__all_':
                self.fields[f].widget.attrs.update({'class': 'error', 'value': ''})
        return form
 
    class Meta:
        fields = ['email', 'username', 'first_name', 'last_name', 'password1',
                  'password2']
        model = User

class AuthenticateForm(AuthenticationForm):
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
 
    def is_valid(self):
        form = super(AuthenticateForm, self).is_valid()
        for f, error in self.errors.iteritems():
            if f != '__all__':
                self.fields[f].widget.attrs.update({'class': 'error', 'value': ''})
        return form

class BeerForm(forms.ModelForm):
    name = forms.CharField(label='Beer Name', required=True, widget=forms.widgets.Textarea(attrs={'class': 'beerName'}))
    rating = forms.CharField(label='Rating', required=True, widget=forms.widgets.Textarea(attrs={'class': 'beerRating'}))

    def is_valid(self):
        form = super(BeerForm, self).is_valid()
        for f in self.errors.iterkeys():
            if f != '__all__':
                self.fields[f].widget.attrs.update({'class': 'error beerText'})
        return form
 
    class Meta:
        model = Beer
        exclude = ('user',)