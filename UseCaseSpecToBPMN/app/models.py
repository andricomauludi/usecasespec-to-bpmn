from django.db import models
from django.forms import ModelForm, Textarea

class projectlist (models.Model):
    no=models.AutoField(primary_key=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    usecasename=models.CharField(max_length=100)
    actor=models.CharField(max_length=100)
    precondition=models.CharField(max_length=100)
    postcondition=models.CharField(max_length=100)
    class Meta:
        db_table="projectlist"

scenariotype_choice = (
    ('task','TASK'),
    ('conditional','Conditional'),
)
class scenariolist (models.Model):
    no=models.AutoField(primary_key=True)
    projectno=models.ForeignKey(projectlist, on_delete=models.CASCADE)
    scenarioid=models.IntegerField(max_length=100)
    scenariotype=models.CharField(max_length=100, choices=scenariotype_choice, default='task')
    scenario=models.CharField(max_length=100)
    prescenarioid=models.IntegerField(max_length=100)
    postscenarioid=models.IntegerField(max_length=100)
    class Meta:
        db_table="scenariolist"
