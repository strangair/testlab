# coding: utf-8

from django.http import Http404, HttpResponse
from django.shortcuts import render, render_to_response

from books.models import Book

# Create your views here.

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html', {'books': books, 'query': q})
    return render_to_response('search_form.html', {'error': error})
