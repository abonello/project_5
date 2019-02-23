from django.conf.urls import url
from .views import issuetracker

urlpatterns = [
    url(r'^$', issuetracker, name='issues'),
]
