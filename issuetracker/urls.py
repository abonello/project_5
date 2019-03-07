from django.conf.urls import url
from .views import issuetracker, issues, create_an_issue, create_a_comment, vote

urlpatterns = [
    url(r'^$', issuetracker, name='issues'),
    url(r'^1$', issues, name='issues1'),
    url(r'^add-issue$', create_an_issue, name="add-issue"),
    url(r'^add-comment/(?P<issue_id>\d+)$', create_a_comment, name="add-comment"),
    url(r'^add-comment$', create_a_comment, name="add-comment"),
    url(r'^vote/(?P<issue_id>\d+)$', vote, name="vote")
    
]
