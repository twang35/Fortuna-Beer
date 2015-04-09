from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from randBeer.forms import AuthenticateForm, UserCreateForm, BeerForm
from search.forms import NameForm
from django.contrib.auth.decorators import login_required

from randBeer.models import Beer


# Create your views here.

def index(request, auth_form=None, user_form=None):
	search_form = NameForm()
	if request.user.is_authenticated():
		beer_form = BeerForm()
		user = request.user
		beers = Beer.objects.filter(user=user.id).order_by('-creation_date')[:5]
		return render(request,
						'index.html',
						{'user': user,
						'beers': beers, 
						'beer_form': beer_form, 
						'search_form': search_form,
						'next_url': '/', })
	else:
		auth_form = auth_form or AuthenticateForm()
		user_form = user_form or UserCreateForm()
		
		return render(request,
				'newUser.html',
				{'auth_form': auth_form,
				'user_form': user_form, 
				'search_form': search_form,})


def favorites(request):
	# reponse = "You are accessing favorite beers with user %s."
	# return HttpResponse(response % user_id)
	return HttpResponse("blah favorites")

def login_view(request):
	if request.method == 'POST':
		form = AuthenticateForm(data=request.POST)
		if form.is_valid():
			login(request, form.get_user())
			# Success
			return redirect('/')
		else:
			# Failure
			return index(request, auth_form=form)
	return redirect('/')
 
def logout_view(request):
	logout(request)
	return redirect('/')

def signup(request):
	user_form = UserCreateForm(data=request.POST)
	if request.method == 'POST':
		if user_form.is_valid():
			username = user_form.clean_username()
			password = user_form.clean_password2()
			user_form.save()
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('/')
		else:
			return index(request, user_form=user_form)
	return redirect('/')

def rate(request):
    if request.method == "POST":
        beer_form = BeerForm(data=request.POST)
        next_url = request.POST.get("next_url", "/")
        if beer_form.is_valid():
            beer = beer_form.save(commit=False)
            beer.name = request.POST.get("beer_name")
            beer.user = request.user
            beer.save()
            return redirect(next_url)
        else:
            return public(request, beer_form)
    return redirect('/')