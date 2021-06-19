from django.shortcuts import render,redirect
from app.models import projectlist, scenariolist
from app.forms import projectform, scenarioform
from app.decorators import unauthenticated_user, allowed_users
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def index(request):
	resultsdisplay=projectlist.objects.all()
	return render(request,'bpmn_list.html',{'resultsdisplay':resultsdisplay})
