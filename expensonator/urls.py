from django.conf.urls import patterns, include, url
from django.contrib import admin

from expensonator.api import ExpenseResource


admin.autodiscover()

expense_resource = ExpenseResource()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'expensonator.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', 'expensonator.views.home'),
    
    url(r'^api/', include(expense_resource.urls)),
)
