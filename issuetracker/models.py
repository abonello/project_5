from django.db import models

# Create your models here.

class Issues(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.TextField()
    posted_by = models.CharField(max_length=50, default='User')
    votes = models.IntegerField()

    def __str__(self):
        return "{}: {} | posted by {}".format(self.title, self.description, self.posted_by)
