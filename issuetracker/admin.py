from django.contrib import admin
from .models import Issue, IssueAdminPage

# Register your models here.
admin.site.register(Issue)
admin.site.register(IssueAdminPage)

