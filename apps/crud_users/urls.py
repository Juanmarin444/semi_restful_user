from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^show/(?P<id>\d+)$', views.show),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^edit_user/(?P<id>\d+)$', views.edit_user),
    url(r'^add_user$', views.add_user),
    url(r'^create$', views.create_user),
    url(r'^delete/(?P<id>\d+)$', views.destroy),
]

app_name = "crud_users"
