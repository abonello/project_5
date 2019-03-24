import datetime
from django.db import models
from django.contrib.auth.models import User


class Issue(models.Model):
    suggestion_choices = ((True, 'Feature'), (False, 'Bug Fix'))
    is_feature = models.BooleanField(blank=False, default=False, choices=suggestion_choices)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    posted_by = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Issues"


class IssueComment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='comment')
    subject = models.CharField(max_length=100, blank=False)
    comment = models.TextField()
    posted_by = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject