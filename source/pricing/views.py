from django.shortcuts import render

# Create your views here.


def plans(request):
    context = {}
    template = 'plans.html'
    return render(request, template, context)