from django.shortcuts import render
from .models import Job

# Create your views here.
def my_projects(request): #return some html to user
	jobs = Job.objects #getting all jobs in the objects class/database
	return render(request, 'jobs/home.html', {'jobs':jobs})
	#pass a list of jobs too with the dict