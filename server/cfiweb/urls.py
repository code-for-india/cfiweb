from django.conf.urls import patterns, include, url
from tastypie.api import Api
from cfiweb.api import ProjectResource

from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(ProjectResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cfiweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)
