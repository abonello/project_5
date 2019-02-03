from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("This is the new Home page.")

def about(request):
    return HttpResponse("This is the ABOUT page.")
