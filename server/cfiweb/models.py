from django.db import models

class Project(models.Model):
	name = models.CharField(max_length=512)
	desc = models.CharField(max_length=1024, null=True)
	ngo_partner = models.CharField(max_length=1024, null=True)
	ngo_poc = models.CharField(max_length=512, null=True)
	cfi_poc = models.CharField(max_length=512, null=True)
	members = models.CharField(max_length=1024, null=True)
