from django.conf.urls import url

from connector.views import onadata_connector

urlpatterns = [
    url(r'^tableau/connector/$', onadata_connector, name='connector'),
]
