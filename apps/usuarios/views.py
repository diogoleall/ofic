from django.shortcuts import render

# Create your views here.

def _login(request):
    template_name = 'usuarios/html'
    context ={}
    return render (request, template_name , context)

