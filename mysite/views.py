from django.http import HttpResponse
from datetime import datetime

def hello(request):
    return HttpResponse('Hello world')

def current_datetime(request):
    now = datetime.now()
    response = "<html><body>Now: %s </body></html>" % now
    return HttpResponse(response)
