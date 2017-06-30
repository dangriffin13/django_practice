from django.http import HttpResponse

def hello(request):
	return HttpResponse("Hello World")
	
def null(request):
	return HttpResponse("Placeholder for the homepage")