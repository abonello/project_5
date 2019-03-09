from django.shortcuts import render, HttpResponse, redirect, reverse
from django.core.mail import send_mail
from django.contrib import messages

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

def uqc_app(request):
    """Display the UniQue Corn App page."""
    return render(request, "uqc-app.html")

def contact(request):
    """Display the contact us page."""
    '''
    send_mail(
        'subject', 
        'email message',
        'from email',
        ['list of recipient emails'],
        fail_silently=False
     )
     '''
    if request.method == 'POST':
        print("POST method used")
        try:
            # print(request.POST.get('subject'))
            subject = request.POST.get('subject')
            print(subject)
            name = request.POST.get('name')
            print(name)
            email = request.POST.get('email')
            print(email)
            message = request.POST.get('message')
            print(message)

            message_body = "Email sent by {} ({}) through the UniQueCorn website.\n\n{}".format(name, email, message)
            # form = ContactForm(request.POST)
            # if form.is_valid():  # All validation rules pass
            # Process the data in form.cleaned_data
            # ...

                # print(form.cleaned_data['subject'])
        #     name = request.form['name']
        #     email = request.form['email']
            # subject = request.form['subject']
        #     message = request.form['message']
        #     msg = Message(subject, sender=email, recipients=[
        #                 app.config['MAIL_DEFAULT_SENDER']])
        #     msg.body = "{} sent the following message through the Nutrition website: \n\n{}".format(
        #         name, message)
        #     mail.send(msg)
        #     return render_template("message_sent.html", name=name, email=email, subject=subject, message=message)
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

    print("GET method used")
    return render(request, "contact.html")



'''
@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    try:
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        msg = Message(subject, sender=email, recipients=[
                      app.config['MAIL_DEFAULT_SENDER']])
        msg.body = "{} sent the following message through the Nutrition website: \n\n{}".format(
            name, message)
        mail.send(msg)
        return render_template("message_sent.html", name=name, email=email, subject=subject, message=message)
    except Exception as e:
        return render_template("message_error.html", email=email)
'''

'''
ERROR EXAMPLE:
smtplib.SMTPRecipientsRefused: {'websiteadmin@anthonybonello.co.uk': (550, b'Verification failed for <anthony@hotmail>\nThe mail server could not deliver mail to anthonybonello_music@hotmail.  The account or domain may not exist, they may be blacklisted, or missing the proper dns entries.\nSender verify failed')}'''
