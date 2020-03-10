from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


# class Announcement(models.Model):
# 	content = models.TextField()
# 	date_posted = models.DateTimeField(auto_now=True)

    		    



    def get_absolute_url(self):
    	# return reverse('post_detail', kwargs= {'pk': self.pk}) # this takes to the blg details 
    	return reverse('blog_home')


 

