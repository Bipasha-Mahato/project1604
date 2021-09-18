from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return render(request, 'login.html')
    #return HttpResponse('this is login page')
def sign_up(request):
    return render(request, 'sign_up.html')
    #return HttpResponse('this is sign_up page')
def sdn_dashboard1(request):
    return render(request, 'sdn_dashboard1.html')
    #return HttpResponse('this is sdn_dashboard1 page')

"""
def login(request):
    return render(request, 'login.html')
def sign_up(request):
    return render(request, 'sign_up.html')
def sdn_dashboard1(request):
    return render(request, 'sdn_dashboard1.html')
"""
