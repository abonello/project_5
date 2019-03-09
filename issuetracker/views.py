# import datetime
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
# import JsonResponse

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
        if form.is_valid():
            print(form.cleaned_data.get('title'))
            print(form.cleaned_data.get('is_feature'))

            if form.cleaned_data.get('is_feature'):
                # This is a feature - PAY if you have money

                # Do you have enough money?
                coin_user = request.user.relateduser.all
                user_coins = get_object_or_404(
                    UserCoins, user=request.user.id)
                print(user_coins)
                print(user_coins.coin_amount)

                if user_coins.coin_amount >= 300:
                    print("You are rich.")
                    user_coins.coin_amount -= 300
                    user_coins.save()
                    print(user_coins.coin_amount)

                    print("You can add the feature.")
                    if form.is_valid() and request.user.is_authenticated():
                        thisForm = form.save()
                        thisForm.posted_by = request.user.username
                        thisForm.save()
                        messages.error(
                            request, "Your new feature has been added.")
                        return redirect(issues)
                else:
                    print("You are very poor. You cannot add a feature.")
                    messages.error(request, "You do not have enough coins. Buy some more if you would like to create a new feature request.")
                    return redirect(all_products)

            else:
                print('pass')
                # This is a bug we will allow you to submit for for free this time.
                
                if form.is_valid() and request.user.is_authenticated():
                    thisForm = form.save()
                    thisForm.posted_by = request.user.username
                    thisForm.save()
                    messages.error(
                        request, "Your new bug has been added.")
                    return redirect(issues)









        # try:
        #     print("PASS")
            # coin_user = request.user.relateduser.all
            # user_coins = get_object_or_404(
            #     UserCoins, user=request.user.id)
            # print(user_coins)
            # print(user_coins.coin_amount)

            # Check coin amount more than 100
            # if user_coins.coin_amount >= 300:
            #     print("You are rich.")
            #     user_coins.coin_amount -= 300
            #     user_coins.save()
            #     print(user_coins.coin_amount)

            #     print("You can add the feature.")
            #     if form.is_valid() and request.user.is_authenticated():
            #         thisForm = form.save()
            #         thisForm.posted_by = request.user.username
            #         thisForm.save()
            #         return redirect(issues)
            # else:
            #     print("You are very poor. You cannot add a feature.")
        # except:
        #     print("Cannot find USER")





        # if form.is_valid() and request.user.is_authenticated():
        #     thisForm = form.save()
        #     thisForm.posted_by = request.user.username
        #     thisForm.save()
        #     return redirect(issues)
    else:  # Return an empty form
        form = IssueItem()

    return render(request, 'add_issue.html', {'form': form})


@login_required
def create_a_comment(request, issue_id):
    
    if request.method == "POST":
        print("This is POST")
        print(issue_id)
        # this_issue = get_object_or_404(
        #     Issue, id=issue_id)
        # print(this_issue)
        form = Comment(request.POST, request.FILES)
        try: 
            if form.is_valid() and request.user.is_authenticated():
                print("Form is Valid")
                # thisForm.issue = issue_id
                # print(form)
                # print(form['subject'].value())
                # print(form['comment'].value())
                # for each in form:
                    # id = each.auto_id
                    # value = each.value()

                # aComment = IssueComment()
                # print("Printing Comment")
                # print(aComment)
                # aComment.subject = form['subject'].value()
                # aComment.comment = form['comment'].value()
                # aComment.posted_by = request.user.username


                # print("Printing Comment again")
                # print(aComment.subject)
                # print(aComment.comment)
                # print(aComment.posted_by)
                # this_issue = get_object_or_404(Issue, id=issue_id)
                # print("get issue")

                # this_issue.comment = IssueComment()
                # this_issue.comment = aComment
                # print("create new comment")
                # this_issue.comment.subject = form['subject'].value()
                # this_issue.comment.comment = form['comment'].value()
                # this_issue.comment.posted_by = request.user.username
                # print("Attached comment but not saved")

                # this_issue.save()
                

                # messages.success(request, "You have successfully registered.")

                thisForm = form.save()
                # print("form is saved")
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
        # print(request.user.username)

        coin_user = request.user.relateduser.all

        user_coins = get_object_or_404(
            UserCoins, user=request.user.id)
        print(user_coins)


        print(user_coins.coin_amount)

        # Check coin amount more than 100
        if user_coins.coin_amount >= 100:
            print("You are rich.")
            user_coins.coin_amount -= 100
            user_coins.save()
            print(user_coins.coin_amount)

            issue = get_object_or_404(Issue, pk=issue_id)
            issue.votes = issue.votes + 1
            issue.save()



        else:
            print("You are very poor.")
            messages.error(
                request, "You do not have enough coins. Buy some more if you would like to vote for features or bugs.")
            return redirect(all_products)

        
    except:
        print("Cannot find USER")
        # print("Cannot find COIN_AMOUNT")
        # print(coins)
        # print(quantity * coins)




    # try:
    #     issue=get_object_or_404(Issue, pk = issue_id)

    #     issue.vote = issue.vote + 1

    #     issue.save()
       
        # if request.method == 'POST':
        #     form = Issue(request.POST, instance=item)
        #     if form.is_valid():
        #         form.save()
        #         return redirect(test_todo_list)
        # else:
        #     form = ItemForm(instance=item)
    # except: 
    #     pass

    # return render(request, 'add_item_django-form.html', {'form': form})
    return redirect(issues)
    # return render(request, "issue_tracker.html", {'issues': allIssues, 'feature_count': feature_count, "bug_count": bug_count})

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
        # I can do this differently by requesting data from db where is_feature is true or false
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

    print("These are the features")
    print(features)
    print("These are the bugs")
    print(bugs)

    data = {
            "Malta": 32,
            "England": 24,
            "France": 28,
            "Italy": 29
        }
    data1 = {}
    data1['features'] = features
    data1['bugs'] = bugs
    print(data1)
    response_data = {}
    try:
        response_data['result'] = 'Success'
        # response_data['message'] = "data to pass to front end"
        response_data['message'] = data1
    except:
        response_data['result'] = 'Error'
        response_data['message'] = 'Something went wrong'
    # return render(request, 'issue_charts.html', {'data': data})
    return HttpResponse(json.dumps(response_data), content_type="application/json")
