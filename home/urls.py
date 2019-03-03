from django.conf.urls import url
from .views import index, about, blog

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^about/$', about, name="about"),
    url(r'^blog/$', blog, name="blog")
]
