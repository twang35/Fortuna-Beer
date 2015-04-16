from django.conf.urls import patterns, include, url
from django.contrib import admin

from randBeer import views as rViews
from suggest import views as sViews
from search import views as bViews

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fortuna.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', rViews.index, name='index'),
    url(r'^favorites/', rViews.favorites, name='favorites'),
    url(r'^suggest/', sViews.suggest, name='suggest'),
    url(r'^signup$', rViews.signup), 
    url(r'^login$', rViews.login_view),  
    url(r'^logout$', rViews.logout_view), 
    url(r'^rate$', rViews.rate),
    url(r'^search/$', bViews.get_name),
    url(r'^detail/(?P<id>[a-zA-Z0-9]{0,20})/$', bViews.detail),
)
