from django.contrib import admin
from .models import Publisher, Author, Book

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name','last_name','email')
	search_fields = ('first_name', 'last_name')
	list_filter = ('last_name',)
	ordering = ('last_name','first_name')
	#fields = ('last_name','first_name', 'email')

admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book)