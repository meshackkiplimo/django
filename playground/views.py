from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request handler
def say_hello(request):
    #use render
    return render(request, 'hello.html',{'name':'kimaiyo'})

