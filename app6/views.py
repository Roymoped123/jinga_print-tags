from django.shortcuts import render

# Create your views here.

def jinja_print(request):
    d=context={'name':'Naresh','age':22}
    return render(request,'jinga_print.html',d)
