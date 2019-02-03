"""UniQueCorn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from testing.views import say_hello, render_test_template, test_todo_list, test_create_an_item, test_create_an_item_django_form, test_edit_an_item, test_toggle_status, test_delete_item
from accounts import urls as accounts_urls
from accounts.views import index
# from accounts.views import index, logout, login, registration, user_profile
from home import urls as home_urls

urlpatterns = [
    url(r'^', include(home_urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^hello$', say_hello),
    url(r'^test$', render_test_template, name="test"),
    url(r'^todo$', test_todo_list, name="todo"),
    url(r'^add$', test_create_an_item),
    url(r'^add_django-form$', test_create_an_item_django_form, name="add"),
    url(r'^edit/(?P<id>\d+)$', test_edit_an_item),
    url(r'^toggle/(?P<id>\d+)$', test_toggle_status),
    url(r'^delete/(?P<id>\d+)$', test_delete_item),
    url(r'^index$', index, name="account_index"),
    # url(r'^accounts/logout/$', logout, name="logout"),
    # url(r'^accounts/login/$', login, name="login"),
    # url(r'^accounts/register/$', registration, name="registration"),
    # url(r'^accounts/profile/$', user_profile, name="profile")
    url(r'^accounts/', include(accounts_urls)),
]
