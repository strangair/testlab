from django.http import Http404, HttpResponse
import datetime

def hello(request):
    return HttpResponse('Hello world')

def current_datetime(request):
    now = datetime.datetime.now()
    response = "<html><body>Now: %s </body></html>" % now
    return HttpResponse(response)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    response = "<html><body>Через %s часов будет%s.</body></html>" % (offset, dt)

    return HttpResponse(response)
