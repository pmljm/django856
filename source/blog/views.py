from django.shortcuts import render

# Create your views here.
def chat(request):
    context = {}
    template = 'chat.html'
    return render(request, template, context)