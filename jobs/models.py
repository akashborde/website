from django.db import models

# Create your models here.

class Job(models.Model): #a job has an image and summary
	# Images
	#create a property to save images
	image = models.ImageField(upload_to='images/') 
	#in parenthesis, where the image will be saved
	# summary
	summary = models.CharField(max_length = 200)
	# how big do we want this char field to take?

	#need to make a migration for this