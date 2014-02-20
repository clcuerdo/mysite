from django.db import models

# Create your models here.
class User(models.Model):
	password = models.CharField(max_length=50)
	email = models.CharField(max_length=100)
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	join_date = models.DateTimeField('join date')

	def __unicode__(self):
		return self.firstname

class Badge(models.Model):
	user = models.ForeignKey(User)
	reputation = models.FloatField()
	badge = models.CharField(max_length=100)

	def __unicode__(self):
		return self.badge

class Submission(models.Model):
	user = models.ForeignKey(User)
	submission_date = models.DateTimeField('submission date')
	latitude = models.FloatField()
	longitude = models.FloatField()
	found = models.BooleanField(default=False)
	details = models.TextField()

	def __unicode__(self):
		return self.details

	def was_found(self):
		return self.found

	was_found.admin_order_field = 'found'
	was_found.admin_order_field = True
	was_found.short_description = 'Found'

class Comment(models.Model):
	user = models.ForeignKey(User)
	submission = models.ForeignKey(Submission)
	latitude = models.FloatField()
	longitude = models.FloatField()
	details = models.TextField()

	def __unicode__(self):
		return self.details