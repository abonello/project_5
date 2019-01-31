from .forms import ItemForm
from .models import Item
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404


def say_hello(request):
    return HttpResponse("Hello World - This is a test")


def render_test_template(request):
    return render(request, "test.html")

@login_required
def test_todo_list(request):
    results = Item.objects.all()
    return render(request, 'todo_list.html', {'items': results})

@login_required
def test_create_an_item(request):
    if request.method =="POST":
        new_item = Item() # instance of the Item model
        new_item.name = request.POST.get('name')
        new_item.done = 'done' in request.POST
        new_item.save()
        return redirect(test_todo_list)

    return render(request, 'add_item_form.html')

@login_required
def test_create_an_item_django_form(request):
    if request.method =="POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(test_todo_list)
    else: # Return an empty form
        form = ItemForm()

    return render(request, 'add_item_django-form.html', {'form': form})

@login_required
def test_edit_an_item(request, id):
    item = get_object_or_404(Item, pk=id)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(test_todo_list)
    else:
        form = ItemForm(instance=item)
        
    return render(request, 'add_item_django-form.html', {'form': form})

@login_required
def test_toggle_status(request, id):
    item = get_object_or_404(Item, pk=id)
    item.done = not item.done
    item.save()
    return redirect(test_todo_list)

@login_required
def test_delete_item(request, id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    return redirect(test_todo_list)
