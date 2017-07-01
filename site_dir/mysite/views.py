from django.http import HttpResponse
import datetime

def hello(request):
	return HttpResponse("Hello World")
	
def null(request):
	return HttpResponse("Placeholder for the homepage")

def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>It's currently %s </body></html>" % now
	return HttpResponse(html)