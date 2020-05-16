from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    current_time = 1111
    return render(request, 'tdee.html', context=locals())
    # return HttpResponse("Hello World!")

def test(request):
    return render(request, 'function1.html', context=locals())