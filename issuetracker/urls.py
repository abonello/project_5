from django.conf.urls import url
from .views import issuetracker, issues

urlpatterns = [
    url(r'^$', issuetracker, name='issues'),
    url(r'^1$', issues, name='issues1'),
]
