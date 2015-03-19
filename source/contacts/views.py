from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

from .forms import signinForm
# Create your views here.
def contact(request):
    context = {}
    template = 'contact.html'
    return render(request, template, context)

