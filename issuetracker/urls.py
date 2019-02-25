from django.conf.urls import url
from .views import issuetracker, issues, create_an_issue, create_a_comment

urlpatterns = [
    url(r'^$', issuetracker, name='issues'),
    url(r'^1$', issues, name='issues1'),
    url(r'^add-issue$', create_an_issue, name="add-issue"),
    url(r'^add-comment$', create_a_comment, name="add-comment"),
]
