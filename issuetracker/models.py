import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Issue(models.Model):
    suggestion_choices = ((True, 'Feature'), (False, 'Bug Fix'))
    is_feature = models.BooleanField(blank=False, default=False, choices=suggestion_choices)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    posted_by = models.CharField(max_length=50)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # posted_by = models.ForeignKey(User, null=False, on_delete=models.PROTECT)
    votes = models.IntegerField(default=0)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        # return "{}: {} | posted by {} @ {} | Feature: {} | Votes: {}".format(self.title, self.description, self.posted_by, self.date_time, self.is_feature, self.votes)

    class Meta:
        verbose_name_plural = "Issues"

class IssueComment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='comment')
    subject = models.CharField(max_length=100, blank=False)
    comment = models.TextField()
    posted_by = models.CharField(max_length=50)
    # user = models.ForeignKey(
    #     User, on_delete=models.CASCADE, related_name='relateduser')
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
        # return "{} posted by {} about issue: {}".format(self.subject, self.user, self.issue)

# class IssueAdminPage(models.Model):
#     status_choices = ((0, "not scheduled"), (1, "scheduled"), (2, "in progress"), (3, "completed"))
#     priority_choices = ((0, "low"), (1, 'normal'), (2, 'high'))

#     issue = models.ForeignKey(Issue, null=False, on_delete=models.CASCADE)
#     status = models.PositiveSmallIntegerField(choices=status_choices, default=0)
#     date_started = models.DateField(null=True, blank=True)
#     date_completed = models.DateField(null=True, blank=True)
#     in_current_voting_cycle = models.BooleanField(blank=False, default=True)
#     was_successful = models.NullBooleanField(blank=True, null=True)
#                         # current_winner = models.BooleanField(blank=False, default=False)

#     def __str__(self):
#         return self.issue.title

    # Code for turning other current_winner values
    # to False once a new value saved as a True
    # Code from: https://stackoverflow.com/questions/1455126/unique-booleanfield-value-in-django
    # def save(self, *args, **kwargs):
    #     if self.current_winner:
    #         try:
    #             temp = IssueAdminPage.objects.get(current_winner=True)
    #             if self != temp:
    #                 temp.current_winner = False
    #                 temp.save()
    #         except IssueAdminPage.DoesNotExist:
    #             pass
    #     super(IssueAdminPage, self).save(*args, **kwargs)

    #     # My code
    #     # For setting completed date automatically once status set to done
    #     if self.status == 3 and self.date_completed is None:
    #         try:
    #             self.date_completed = datetime.date.today()

    #         except IssueAdminPage.DoesNotExist:
    #             pass
    #     super(IssueAdminPage, self).save(*args, **kwargs)






# class Issue(models.Model):
#     title = models.CharField(max_length=100, default='')
#     description = models.TextField()
#     # posted_by = models.CharField(max_length=50, default='User')
#     posted_by = models.CharField(max_length=50)

#     votes = models.IntegerField(default=0)

#     def __str__(self):
#         return "{}: {} | posted by {}".format(self.title, self.description, self.posted_by)

#     class Meta:
#         verbose_name_plural = "Issues"
