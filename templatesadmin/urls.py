from django.conf.urls import url

urlpatterns = [
    url(r'^$', templatesadmin.views.listing, name='templatesadmin-overview'),
    url(r'^edit(?P<path>.*)/$', templatesadmin.views.modify, name='templatesadmin-edit'),
]
