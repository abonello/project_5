from django.shortcuts import render, HttpResponse

# Create your views here.
def say_hello(request):
    return HttpResponse("Hello World - This is a test")

def render_test_template(request):
    return render(request, "test.html")