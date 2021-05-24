from django.shortcuts import render,redirect
from app.models import projectlist, scenariolist
from app.forms import projectform, scenarioform
# Create your views here.

def index(request):
	resultsdisplay=projectlist.objects.all()
	return render(request,'project_list.html',{'resultsdisplay':resultsdisplay})

def createproject(request):
    form=projectform()
    if request.method == 'POST':
       form=projectform(request.POST)
       if form.is_valid():
           form.save()
           return redirect('/project_list')
    context = {'form':form}
    return render (request, 'project_list_form.html',context)

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


def indexscenario(request):
	scenariodisplay=scenariolist.objects.all()
	return render(request,'scenario_list.html',{'scenariodisplay':scenariodisplay})

def createscenario(request):
    form=scenarioform()
    if request.method == 'POST':
       form=scenarioform(request.POST)
       if form.is_valid():
           form.save()
           return redirect('/project_list/scenario_list')
    context = {'form':form}
    return render (request, 'scenario_list_form.html',context)

def updatescenario(request,pk):
    scenarioupdate=scenariolist.objects.get(no=pk)
    form=scenarioform(instance=scenarioupdate)
    if request.method == 'POST':
       form=scenarioform(request.POST,instance=scenarioupdate)
       if form.is_valid():
           form.save()
           return redirect('/project_list/scenario_list')
    context = {'form':form}
    return render (request, 'scenario_list_form.html',context)

def deletescenario(request,pk):
    scenariodel=scenariolist.objects.get(no=pk)
    scenariodel.delete()
    return redirect('/project_list/scenario_list')
