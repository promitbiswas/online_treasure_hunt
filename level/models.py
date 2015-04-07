from django.db import models
from fandjango.models import User

class level(models.Model):
	number = models.IntegerField()
	slug = models.SlugField()
	title = models.CharField(max_length=200)
	source = models.TextField()
	photo = models.ImageField(upload_to='images/')
	text = models.TextField()
	js = models.TextField()
	answer = models.CharField(max_length=200)

	def __unicode__(self):
		return self.slug

class over(models.Model):
	winner = models.ForeignKey(User)

	def __unicode__(self):
		return self.winner.first_name
