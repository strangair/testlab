from django.shortcuts import render, render_to_response

# Create your views here.

def search_form(request):
    return render_to_response('search_form.html')

