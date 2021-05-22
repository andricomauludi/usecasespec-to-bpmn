from django.db import models
from django.forms import ModelForm, Textarea

class projectlist (models.Model):
    no=models.IntegerField(primary_key=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    usecasename=models.CharField(max_length=100)
    actor=models.CharField(max_length=100)
    precondition=models.CharField(max_length=100)
    postcondition=models.CharField(max_length=100)
    class Meta:
        db_table="projectlist"