from django.conf.urls import url, include
from .apps.recognition import urls as recognition_urls
from .apps.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^recognition/', include(recognition_urls)),
]
