from django.db import models

class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField()

	def __str__(self):
		return '%s, %s' % (self.name, self.website)

	class Meta:
		ordering = ['name']

class Author(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField(blank=True, verbose_name= 'E-mail')

	def __str__(self):
		return '%s, %s' % (self.last_name, self.first_name)

	class Meta:
		ordering = ['last_name']

class Book(models.Model):
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	publication_date = models.DateField(blank=True, null=True)

	def __str__(self):
		return '%s, %s' % (self.title, self.publisher)

	class Meta:
		ordering = ['title']