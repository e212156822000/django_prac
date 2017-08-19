from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Article(models.Model):
	title = models.CharField(max_length=200)
	pub_date = models.DateField()

	def get_absolute_url(self):
		return reverse('article-detail', kwargs={'pk': self.pk})

