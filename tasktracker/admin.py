from django.contrib import admin

from .models import ProjectMaster, TaskMaster

admin.site.register(ProjectMaster)
admin.site.register(TaskMaster)
