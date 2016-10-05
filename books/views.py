# coding: utf-8

from django.shortcuts import render, render_to_response

# Create your views here.

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET:
        message = 'Вы искали: %r' % request.GET['q']
    else:
        message = 'Вы отправили пустую форму.'
    return HttpResponse(message)