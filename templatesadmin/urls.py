from django.conf.urls import url
from templatesadmin.views import listing, modify

urlpatterns = [
    url(r'^$', listing, name='templatesadmin-overview'),
    url(r'^edit(?P<path>.*)/$', modify, name='templatesadmin-edit'),
]
