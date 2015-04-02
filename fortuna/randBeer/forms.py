from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from randBeer.models import Beer

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-signup', 'placeholder': 'Email'}))
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'class': 'form-signup', 'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'class': 'form-signup', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'class': 'form-signup', 'placeholder': 'Password Confirmation'}))
 
    def is_valid(self):
        form = super(UserCreateForm, self).is_valid()
        for f, error in self.errors.iteritems():
            if f != '__all_':
                self.fields[f].widget.attrs.update({'class': 'error', 'value': ''})
        return form
 
    class Meta:
        fields = ['email', 'username', 'password1',
                  'password2']
        model = User

class AuthenticateForm(AuthenticationForm):
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'id': 'login-username', 'class': 'form-login', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'id': 'login-password', 'class': 'form-login', 'placeholder': 'Password'}))
 
    def is_valid(self):
        form = super(AuthenticateForm, self).is_valid()
        for f, error in self.errors.iteritems():
            if f != '__all__':
                self.fields[f].widget.attrs.update({'class': 'error', 'value': ''})
        return form

class BeerForm(forms.ModelForm):
    CHOICES = (('1', '1 Star'), ('2', '2 Star'), ('3', '3 Star'), ('4', '4  Star'), ('5', '5 Star'))
    rating = forms.ChoiceField(label='Rating', required=True, widget=forms.RadioSelect, choices=CHOICES)

    def is_valid(self):
        form = super(BeerForm, self).is_valid()
        for f in self.errors.iterkeys():
            if f != '__all__':
                self.fields[f].widget.attrs.update({'class': 'error beerText'})
        return form
 
    class Meta:
        model = Beer
        exclude = ('user','name')