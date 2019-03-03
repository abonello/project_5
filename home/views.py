from django.shortcuts import render, HttpResponse

def index(request):
    """Display the home page."""
    return render(request, "index_home.html")
    # return HttpResponse("This is the new Home page.")

def about(request):
    """Display the about page."""
    return render(request, "about.html")
    # return HttpResponse("This is the ABOUT page.")

def blog(request):
    """Display the blog page."""
    return render(request, "blog.html")
