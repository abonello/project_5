# import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import IssueItem, Comment
from .models import Issue, IssueComment

# Create your views here.
@login_required()
def issuetracker(request):
    """ Hard Coded Data """
    issues = [
        {
            'id': '1',
            'title': "First Feature Request",
            'description': "I need this functionality added that when I press the button it goes in turbo mode and produces double the amount of corn",
            'posted_by': "AlfaAlfa",
            'votes': "5"
        },
        {
            'id': '2',
            'title': "Popcorn maker",
            'description': "I would like the app to pop the corns ready to eat. I am fed up having to cook them.",
            'posted_by': "Bastard",
            'votes': "20"
        },
        {
            'id': '3',
            'title': "Colored Corn",
            'description': "I would like to be able to choose the color of the corn produced, nut just the boring natural color.",
            'posted_by': "Complainer",
            'votes': "1"
        }

    ]

    # print(issues.values)
    return render(request, "issue_tracker.html", {'issues': issues})

@login_required()
def issues(request):
    """ Gets Data form database """
    # allIssues = Issue.objects.all().prefetch_related('relatedissue')
    allIssues = Issue.objects.all()
    # print(Issue.objects.get(id=1).comment.all())
    feature_count = 0
    bug_count = 0

    for each in allIssues:
        # I can do this differently by requesting data from db where is_feature is true or false
        if each.is_feature:
            feature_count += 1
        else:
            bug_count += 1
    


    return render(request, "issue_tracker.html", {'issues': allIssues, 'feature_count': feature_count, "bug_count": bug_count})


@login_required
def create_an_issue(request):
    if request.method == "POST":
        form = IssueItem(request.POST, request.FILES)
        # if request.user.is_authenticated():
        #     print("User is authenticated")
        if form.is_valid() and request.user.is_authenticated():
            thisForm = form.save()
            thisForm.posted_by = request.user.username
            thisForm.save()
            return redirect(issues)
    else:  # Return an empty form
        form = IssueItem()

    return render(request, 'add_issue.html', {'form': form})


@login_required
def create_a_comment(request):
    if request.method == "POST":
        form = Comment(request.POST, request.FILES)
        if form.is_valid() and request.user.is_authenticated():
            thisForm = form.save()
            thisForm.posted_by = request.user.username
            thisForm.save()
            return redirect(issues)
    else:  # Return an empty form
        form = Comment()
    return render(request, 'add_comment.html', {'form': form})
