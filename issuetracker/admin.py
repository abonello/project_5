from django.contrib import admin
from .models import Issue, IssueComment

# Register your models here.
admin.site.register(Issue)
admin.site.register(IssueComment)