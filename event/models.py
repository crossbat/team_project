from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Notification(models.Model):
	subject = models.CharField(max_length = 200)
	writer = models.CharField(default = "관리자",max_length = 200)
	content = RichTextUploadingField('내용', blank=True, null=True)
	create_date = models.DateField()

	def __str__(self):
		return self.subject

