# coding: utf-8

from django.http import Http404, HttpResponse
from django.shortcuts import render, render_to_response

from mysite.books.models import Book

# Create your views here.

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render_to_response('search_results.html', {'books': books, 'query': q})
    else:
        message = 'Вы отправили пустую форму.'
    return HttpResponse(message)