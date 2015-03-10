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

def team(request):
    context = {}
    template = 'team.html'
    return render(request, template, context)