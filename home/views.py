from django.shortcuts import render, HttpResponse, redirect, reverse
from django.core.mail import send_mail
from django.contrib import messages

def index(request):
    """Display the home page."""
    return render(request, "index_home.html")

def about(request):
    """Display the about page."""
    return render(request, "about.html")

def blog(request):
    """Display the blog page."""
    return render(request, "blog.html")

def uqc_app(request):
    """Display the UniQue Corn App page."""
    return render(request, "uqc-app.html")

def contact(request):
    """Display the contact us page."""

    if request.method == 'POST':
        try:
            subject = request.POST.get('subject')
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')

            message_body = "Email sent by {} ({}) through the UniQueCorn website.\n\n{}".format(name, email, message)
            
        except Exception as e:
            messages.error(request, "Your email has failed.")
            return redirect(reverse('index'))

        send_mail(
            subject, 
            message_body,
            'websiteadmin@anthonybonello.co.uk',
            ['websiteadmin@anthonybonello.co.uk'],
            fail_silently=False
        )
        messages.success(request, "You have sent an email successfully.")
        return redirect(reverse('index'))

    return render(request, "contact.html")