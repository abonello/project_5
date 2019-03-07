from django import forms
from .models import Issue, IssueComment


class IssueItem(forms.ModelForm):
    class Meta:
        model = Issue
        # fields = ('title', 'description', 'posted_by')
        fields = ('is_feature', 'title', 'description')
        labels = {
            'is_feature': ('Feature or Bug?'),
        }
        # self.fields['is_feature'].label = "Feature or Bug?"
        # widgets = {"user": forms.HiddenInput()}  # value set in views
        widgets = {"posted_by": forms.HiddenInput()}  # value set in views
        widgets = {"votes": forms.HiddenInput()}  # value set in views
        widgets = {"date_time": forms.HiddenInput()}  # value set in views



# class SuggestionForm(forms.ModelForm):
#     class Meta:
#         model = Suggestion
#         exclude = ["date_time"]
#         widgets = {"user": forms.HiddenInput()}  # value set in views
#         labels = {
#             "is_feature": "Suggestion Type",
#             "delay_submission": "Delay Submission Till Next Voting Cycle<br> If you're worried that you won't be able to catch up with the current leaders"
#         }
class Comment(forms.ModelForm):
    class Meta:
        model = IssueComment
        fields = ('issue', 'subject', 'comment')
        widgets = {"posted_by": forms.HiddenInput()}  # value set in views
        widgets = {"date_time": forms.HiddenInput()}  # value set in views
        # widgets = {"issue": forms.HiddenInput()}  # value set in views
