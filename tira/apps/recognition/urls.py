from django.conf.urls import url

from . import views

app_name = 'recognition'
urlpatterns = [
    url(r'^$', views.images, name='images'),
    url(r'images$', views.images, name='images'),
]