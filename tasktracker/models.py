from django.db import models


class ProjectMaster(models.Model):
    project_title = models.CharField(max_length=75)
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.project_title


class TaskMaster(models.Model):
    task_name = models.CharField(max_length=120)
    task_date = models.DateField(auto_now_add=True)
    starttimestamp = models.TimeField()
    endtimestamp = models.TimeField()
    ac_starttimestamp = models.TimeField(null=True, blank=True)
    ac_endtimestamp = models.TimeField(null=True, blank=True)
    projecttitle = models.ForeignKey(ProjectMaster, on_delete=models.CASCADE)
