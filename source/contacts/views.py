from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

from .forms import contactForm
# Create your views here.
def contact(request):
    ''' def contact is rendering are contact HTML and are future form, I am adding
    a email validation to this view, so when future user sign/login or sent a massage,
    you will be receving an email from user to your email.
    Note: You need to define your email credential in django settings.py '''
    title = 'Contact'
    form = contactForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        comment = form.cleaned_data['comment']
        name = form.cleaned_data['name']
        subject = 'Message from MYSITE.com'
        message = '%s %s' % (comment, name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
        title = "Tanks"
        confirm_message = "Tanks for the message!"
        form = None

    context = {'title': title, 'form': form, 'confirm_message': confirm_message}
    template = 'contact.html'
    return render(request, template, context)