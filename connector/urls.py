from django.conf.urls import url
from connector import views

urlpatterns = [
    url(r'^connector$', views.onadata_connector, name='connector'),
]
