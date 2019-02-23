from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Issue

# Create your views here.
@login_required()
def issuetracker(request):
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
    allIssues = Issue.objects.all()
    print(allIssues[0])
    # issues = [
    #     {
    #         'id': '5',
    #         'title': "Test Feature Request",
    #         'description': "This is a Test",
    #         'posted_by': "Test User",
    #         'votes': "500"
    #     },
    # ]

    # print(issues.values)
    return render(request, "issue_tracker.html", {'issues': allIssues})

