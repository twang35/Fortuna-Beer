from django.conf.urls import patterns, url

from randBeer import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
)