from django.shortcuts import render,redirect
from app.models import projectlist, scenariolist
from app.forms import projectform, scenarioform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from app.decorators import unauthenticated_user, allowed_users
# Create your views here.

@login_required(login_url='login')
def index(request):
	resultsdisplay=projectlist.objects.all()
	return render(request,'project_list.html',{'resultsdisplay':resultsdisplay})

@login_required(login_url='login')
def createproject(request):
    form=projectform()
    if request.method == 'POST':
       form=projectform(request.POST)
       if form.is_valid():
           form.save()
           return redirect('/project_list')
    context = {'form':form}
    return render (request, 'project_list_form.html',context)

@login_required(login_url='login')
def updateproject(request,pk):
    projectupdate=projectlist.objects.get(no=pk)
    form=projectform(instance=projectupdate)
    if request.method == 'POST':
       form=projectform(request.POST,instance=projectupdate)
       if form.is_valid():
           form.save()
           return redirect('/project_list')
    context = {'form':form}
    return render (request, 'project_list_form.html',context)

@login_required(login_url='login')
def indexscenario(request,no):
	scenariodisplay=scenariolist.objects.filter(projectno_id=no)
	return render(request,'scenario_list.html',{'scenariodisplay':scenariodisplay})

@login_required(login_url='login')
def createscenario(request):
    form=scenarioform()
    if request.method == 'POST':
       form=scenarioform(request.POST)
       if form.is_valid():
           form.save()
           scenarioupdate=scenariolist.objects.latest('no')
           return redirect('index', no=scenarioupdate.projectno_id)
    context = {'form':form}
    return render (request, 'scenario_list_form.html',context)


@login_required(login_url='login')
def updatescenario(request,pk):
    scenarioupdate=scenariolist.objects.get(no=pk)
    form=scenarioform(instance=scenarioupdate)
    if request.method == 'POST':
       form=scenarioform(request.POST,instance=scenarioupdate)
       if form.is_valid():
           form.save()
           return redirect('index', no=scenarioupdate.projectno_id)
    context = {'form':form}
    return render (request, 'scenario_list_form.html',context)

@login_required(login_url='login')
def deletescenario(request,pk):
    scenariodel=scenariolist.objects.get(no=pk)
    hantu = scenariolist.objects.filter(no=pk).values_list('projectno_id', flat=True).first()
    scenariodel.delete()
    return redirect('index', no=scenariodel.projectno_id)
