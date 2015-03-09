from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    template = 'home.html'
    return render(request, template, context)

def work(request):
    context = {}
    template = 'work.html'
    return render(request, template, context)

def plans(request):
    context = {}
    template = 'plans.html'
    return render(request, template, context)