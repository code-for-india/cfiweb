from tastypie.resources import ModelResource
from cfiweb.models import Project

class ProjectResource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
	resource_name = 'project'
