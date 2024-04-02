from django.urls import re_path

from connector.views import onadata_connector

urlpatterns = [
    re_path(r"^tableau/connector/$", onadata_connector, name="connector"),
]
