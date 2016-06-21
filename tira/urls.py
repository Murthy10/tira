from django.conf.urls import url, include
from .apps.recognition import urls as recognition_urls


urlpatterns = [
    url(r'^recognition/', include(recognition_urls)),
]
