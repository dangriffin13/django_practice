from django.contrib import admin
from .models import Publisher, Author, Book

#superusers: dpg

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name','last_name','email','id')
	search_fields = ('first_name', 'last_name')
	list_filter = ('last_name',)
	ordering = ('last_name','first_name')
	#fields = ('last_name','first_name', 'email')

class PublisherAdmin(admin.ModelAdmin):
	list_display = ('name','website','city','id')
	search_fields = ('name', 'city')
	ordering = ('name',)

class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'publisher', 'publication_date')
	list_filter = ('publication_date',)
	date_hierarchy = 'publication_date'
	search_fields = ('title',)
	ordering = ('title',)

admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)