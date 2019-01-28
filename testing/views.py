from .models import Item
from django.shortcuts import render, HttpResponse


def say_hello(request):
    return HttpResponse("Hello World - This is a test")


def render_test_template(request):
    return render(request, "test.html")


def test_todo_list(request):
    results = Item.objects.all()
    return render(request, 'todo_list.html', {'items': results})
