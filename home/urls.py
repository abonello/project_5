from django.conf.urls import url
from .views import index, about, blog, uqc_app, contact

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^about/$', about, name="about"),
    url(r'^blog/$', blog, name="blog"),
    url(r'^uqc_app/$', uqc_app, name="uqc_app"),
    url(r'^contact/$', contact, name="contact_us")
]