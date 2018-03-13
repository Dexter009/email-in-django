from django.conf.urls import include, url
from django.contrib import admin

import myapp.views

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'newproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/',admin.site.urls),
    url(r'^$', myapp.views.index,name='index'),
]
