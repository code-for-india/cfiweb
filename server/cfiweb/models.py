from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
	name = models.CharField(max_length=512)
	desc = models.CharField(max_length=1024, null=True)
	ngo_partner = models.CharField(max_length=1024, null=True)
	ngo_poc = models.CharField(max_length=512, null=True)
	cfi_poc = models.CharField(max_length=512, null=True)
	members = models.CharField(max_length=1024, null=True)

class Profile(models.Model):
	user = models.OneToOneField(User)
	title = models.CharField(max_length=512, null=True)
	organization = models.CharField(max_length=512, null=True)
	location = models.CharField(max_length=512, null=True)
	skills = models.CharField(max_length=1024, null=True)
	fb_id = models.CharField(max_length=512, null=True)
	linkedin_id = models.CharField(max_length=512, null=True)
	github_id = models.CharField(max_length=512, null=True)
