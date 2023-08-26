from django.db import models

class Notification(models.Model):
	subject = models.CharField(max_length = 200)
	writer = models.CharField(default = "관리자",max_length = 200)
	content = models.TextField()
	create_date = models.DateField()

	def __str__(self):
		return self.subject


class News(models.Model):
	subject = models.CharField(max_length = 200)
	writer = models.CharField(default = "관리자", max_length = 200)
	content = models.TextField()
	create_date = models.DateField()

	def __str__(self):
		return self.subject
