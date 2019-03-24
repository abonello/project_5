from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count
from django.contrib import messages
from .forms import IssueItem, Comment
from accounts.models import UserCoins
from products.views import all_products
from .models import Issue, IssueComment
import json


@login_required()
def issues(request):
    """ Gets Data form database """
    allIssues = Issue.objects.all()
    feature_count = 0
    bug_count = 0

    for each in allIssues:
        if each.is_feature:
            feature_count += 1
        else:
            bug_count += 1
    
    return render(request, "issue_tracker.html", {'issues': allIssues, 'feature_count': feature_count, "bug_count": bug_count})


@login_required
def create_an_issue(request):
    if request.method == "POST":
        form = IssueItem(request.POST, request.FILES)
        if form.is_valid():

            if form.cleaned_data.get('is_feature'):
                '''This is a feature - PAY if you have money'''

                # Do you have enough money?
                coin_user = request.user.relateduser.all
                user_coins = get_object_or_404(
                    UserCoins, user=request.user.id)

                if user_coins.coin_amount >= 300:
                    user_coins.coin_amount -= 300
                    user_coins.save()

                    if form.is_valid() and request.user.is_authenticated():
                        thisForm = form.save()
                        thisForm.posted_by = request.user.username
                        thisForm.save()
                        messages.error(
                            request, "Your new feature has been added.")
                        return redirect(issues)
                else:
                    messages.error(request, "You do not have enough coins. Buy some more if you would like to create a new feature request.")
                    return redirect(all_products)

            else:

                if form.is_valid() and request.user.is_authenticated():
                    thisForm = form.save()
                    thisForm.posted_by = request.user.username
                    thisForm.save()
                    messages.error(
                        request, "Your new bug has been added.")
                    return redirect(issues)

    else:  # Return an empty form
        form = IssueItem()

    return render(request, 'add_issue.html', {'form': form})


@login_required
def create_a_comment(request, issue_id):
    
    if request.method == "POST":
        form = Comment(request.POST, request.FILES)
        try: 
            if form.is_valid() and request.user.is_authenticated():
                thisForm = form.save()
                thisForm.posted_by = request.user.username
                thisForm.save()
                this_issue = get_object_or_404(
                    Issue, id=issue_id)
                this_issue.comments_count = this_issue.comments_count + 1
                this_issue.save()
                return redirect(issues)
        except:
            print("Form is not valid")
    else:  # Return an empty form
        print("This is GET")
        this_issue = get_object_or_404(
            Issue, id=issue_id)
        print(this_issue)
        form = Comment()
    return render(request, 'add_comment.html', {'form': form, 'id_issue': issue_id, 'issue_subject': this_issue })

@login_required
def vote(request, issue_id):
    print("Vote Received")
    try:
        coin_user = request.user.relateduser.all
        user_coins = get_object_or_404(
            UserCoins, user=request.user.id)

        # Check coin amount more than 100
        if user_coins.coin_amount >= 100:
            user_coins.coin_amount -= 100
            user_coins.save()
            issue = get_object_or_404(Issue, pk=issue_id)
            issue.votes = issue.votes + 1
            issue.save()

        else:
            messages.error(
                request, "You do not have enough coins. Buy some more if you would like to vote for features or bugs.")
            return redirect(all_products)

        
    except:
        '''Cannot find USER'''
        pass
        
    return redirect(issues)


def charts(request):
    return render(request, 'issue_charts.html', {})


def get_chart_data(request):
    print("Reached the get_chart_data function")
    allIssues = Issue.objects.all()
    
    feature_count = 0
    bug_count = 0

    features = []
    bugs = []

    for each in allIssues:
        if each.is_feature:
            feature_count += 1
            item = {}
            item['title'] = each.title
            item['votes'] = each.votes
            item['comments'] = each.comments_count
            features.append(item)
        else:
            bug_count += 1
            item = {}
            item['title'] = each.title
            item['votes'] = each.votes
            item['comments'] = each.comments_count
            bugs.append(item)

    data = {}
    data['features'] = features
    data['bugs'] = bugs
    response_data = {}
    try:
        response_data['result'] = 'Success'
        response_data['message'] = data
    except:
        response_data['result'] = 'Error'
        response_data['message'] = 'Something went wrong'
    return HttpResponse(json.dumps(response_data), content_type="application/json")