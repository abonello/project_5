from .forms import ItemForm
from .models import Item
from django.shortcuts import render, HttpResponse, redirect


def say_hello(request):
    return HttpResponse("Hello World - This is a test")


def render_test_template(request):
    return render(request, "test.html")


def test_todo_list(request):
    results = Item.objects.all()
    return render(request, 'todo_list.html', {'items': results})


def test_create_an_item(request):
    if request.method =="POST":
        new_item = Item() # instance of the Item model
        new_item.name = request.POST.get('name')
        new_item.done = 'done' in request.POST
        new_item.save()
        return redirect(test_todo_list)

    return render(request, 'add_item_form.html')


def test_create_an_item_django_form(request):
    if request.method =="POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(test_todo_list)
    else: # Return an empty form
        form = ItemForm()

    return render(request, 'add_item_django-form.html', {'form': form})
