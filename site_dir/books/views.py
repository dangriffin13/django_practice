from django.shortcuts import render



def search_form(request):
	return render(request, 'books/search_form.html')
