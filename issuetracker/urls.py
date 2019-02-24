from django.conf.urls import url
from .views import issuetracker, issues, create_an_issue

urlpatterns = [
    url(r'^$', issuetracker, name='issues'),
    url(r'^1$', issues, name='issues1'),
    url(r'^add-issue$', create_an_issue, name="add-issue"),
]
