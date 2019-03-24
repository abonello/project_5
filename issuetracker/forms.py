from django import forms
from .models import Issue, IssueComment


class IssueItem(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('is_feature', 'title', 'description')
        labels = {
            'is_feature': ('Feature or Bug?'),
        }
        widgets = {"posted_by": forms.HiddenInput()}  # value set in views
        widgets = {"votes": forms.HiddenInput()}  # value set in views
        widgets = {"date_time": forms.HiddenInput()}  # value set in views


class Comment(forms.ModelForm):
    class Meta:
        model = IssueComment
        fields = ('issue', 'subject', 'comment')
        widgets = {"posted_by": forms.HiddenInput()}  # value set in views
        widgets = {"date_time": forms.HiddenInput()}  # value set in views