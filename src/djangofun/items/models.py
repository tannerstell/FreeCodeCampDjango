from django.db import models

# Create your models here.

class Item(models.Model):
	name 		= models.TextField(max_length=100)
	description = models.TextField(blank=True,null=True)
	completed 	= models.BooleanField(default=False)