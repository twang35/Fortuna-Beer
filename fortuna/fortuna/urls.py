from django.conf.urls import patterns, include, url
from django.contrib import admin

from randBeer import views as rViews
from suggest import views as sViews

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fortuna.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', rViews.index, name='index'),
    url(r'^favorites/', rViews.favorites, name='favorites'),
    url(r'^suggest/', sViews.suggest, name='suggest'),
)
