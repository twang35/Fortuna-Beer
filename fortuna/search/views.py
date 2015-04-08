from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import NameForm

def get_name(request):

    if request.method == 'GET':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.GET)
        if form.is_valid():
            searchName = form.cleaned_data['searchBeer']
#            render(request, 'base.html', {'form': form})
            return render(request, 'search.html', {'form': form,
                                                  'searchName': searchName})

    else:
        form = NameForm()
        

    return render(request, 'search.html', {'form': form})