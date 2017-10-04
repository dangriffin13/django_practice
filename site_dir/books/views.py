from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book


#def search_form(request):
	#return render(request, 'books/search_form.html')

def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('You must submit a search term.')
		elif len(q) > 25:
			errors.append('Please enter a search that\'s no longer than 25 characters.')
		else:
			books = Book.objects.filter(title__icontains=q)
			return render(request, 'books/search_results.html', {'books': books, 'query': q})
	return render(request, 'books/search_form.html', {'errors': errors})
