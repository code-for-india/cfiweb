from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from cfiweb.models import Project, Profile

class ProjectResource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
	resource_name = 'project'

class UserResource(ModelResource):
    class Meta:
	queryset = User.objects.all()
	resource_name = 'user'

class ProfileResource(ModelResource):
    class Meta:
	queryset = Profile.objects.all()
	resource_name = 'profile'
