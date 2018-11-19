from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<em>My Second Project</em>")

def help(request):
    my_dict = {'title':"Help Page"}
    return render(request,'AppTwo/help.html',my_dict)
