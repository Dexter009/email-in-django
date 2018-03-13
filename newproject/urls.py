from django.conf.urls import include, url
from django.contrib import admin

import myapp
from myapp import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'newproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'home/',myapp.views.index,name='index'),
]
