from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import NameForm

def get_name(request):

	if request.method == 'GET':
		# create a form instance and populate it with data from the request:
		search_form = NameForm(request.GET)
		if search_form.is_valid():
			searchName = search_form.cleaned_data['searchBeer']
			return render(request, 'search.html', {'search_form': search_form,
													'searchName': searchName})

	else:
		search_form = NameForm()
		

	return render(request, 'search.html', {'search_form': search_form})