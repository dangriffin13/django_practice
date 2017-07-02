from django.http import HttpResponse
from django.template import Template, Context
import datetime

def hello(request):
	return HttpResponse("Hello World")
	
def null(request):
	return HttpResponse("Placeholder for the homepage")

def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>It's currently %s </body></html>" % now
	return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body> In %s hours, it will be %s. </body></html>" % (offset, dt)
	return HttpResponse(html)