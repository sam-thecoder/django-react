from django.db import models

class DadJokes(models.Model):
	text = models.TextField()

	def __str__(self):
		return self.text
