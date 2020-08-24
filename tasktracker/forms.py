from django import forms
from .models import TaskMaster, ProjectMaster

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']


def __init__(self, *args, **kwargs):
    super(RegisterUserForm, self).__init__(*args, **kwargs)

    for fieldname in ['username', 'password1', 'password2']:
        self.fields[fieldname].help_text = None


class ProjectForm(ModelForm):
    class Meta:
        model = ProjectMaster
        fields = ('project_title',)

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['project_title'].required = False


class TaskForm(forms.ModelForm):

    class Meta:
        model = TaskMaster
        fields = ('task_name', 'starttimestamp',
                  'endtimestamp', 'projecttitle')

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['projecttitle'].empty_label = 'Select Project'
        self.fields['starttimestamp'].required = False
        self.fields['endtimestamp'].required = False
        self.fields['projecttitle'].required = False


class TimerForm(forms.ModelForm):

    class Meta:
        model = TaskMaster
        fields = ('ac_starttimestamp', 'ac_endtimestamp')

    def __init__(self, *args, **kwargs):
        super(TimerForm, self).__init__(*args, **kwargs)
        self.fields['ac_starttimestamp'].required = False
        self.fields['ac_endtimestamp'].required = False
