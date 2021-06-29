from django.shortcuts import render,redirect
from app.models import projectlist, scenariolist
from app.forms import projectform, scenarioform
import xml.etree.ElementTree as ET
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
def deleteproject(request,pk):
    projectdel=projectlist.objects.get(no=pk)
    projectdel.delete()
    return redirect('/project_list')

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

def coba(request,pk):
    scenariodisplay=scenariolist.objects.all().filter(projectno_id=pk)
    normal = 0
    for x in scenariodisplay:
        if x.scenariotype == "conditional":
            normal= normal + 1
    if normal == 1:
        jumlahisi=0
        y = 0
        for x in scenariodisplay:
            jumlahisi=jumlahisi+1

        for x in scenariodisplay:
            if x.scenariotype == "task":
                y= y+1
            else:
                break
        Nama = projectlist.objects.filter(no=pk)
        ScenarioHasil1= scenariolist.objects.filter(projectno_id=pk).exclude(postscenarioidyes=y+1)
        ScenarioHasil= scenariolist.objects.filter(projectno_id=pk).exclude(postscenarioidno=y+1)
        return render(request,'BPMN.html',{'ScenarioHasil':ScenarioHasil, 'ScenarioHasil1' :  ScenarioHasil1, 'Nama' : Nama})

    elif normal == 2:
        jumlahisi=0
        y=0
        x1=0
        x2=0
        task=0
        for x in scenariodisplay:
            jumlahisi=jumlahisi+1

        for x in scenariodisplay:
            y= y+1
            if x.scenariotype == "conditional":
                if task==0:
                    x1=y
                    task=task+1
                else:    
                    x2=y
        ScenarioH= scenariolist.objects.filter(projectno_id=pk).get(scenarioid=x2)
        if ScenarioH.postscenarioidyes==x1:
            Nama = projectlist.objects.filter(no=pk)
            ScenarioHasil1= scenariolist.objects.filter(projectno_id=pk).exclude(postscenarioidyes=x1).exclude(postscenarioidno=x2).exclude(postscenarioidyes=x2)
            ScenarioHasil= scenariolist.objects.filter(projectno_id=pk).exclude(postscenarioidno=x1).exclude(postscenarioidno=x2).exclude(postscenarioidyes=x2).exclude(scenarioid__gt=x2)
            ScenarioHasil2= scenariolist.objects.filter(projectno_id=pk).exclude(postscenarioidyes=x2).exclude(postscenarioidno=x1)
            ScenarioHasil3= scenariolist.objects.filter(projectno_id=pk).exclude(postscenarioidno=x2).exclude(postscenarioidno=x1)
            return render(request,'BPMN.html',{'ScenarioHasil':ScenarioHasil, 'ScenarioHasil1' :  ScenarioHasil1, 'Nama' : Nama 
        ,'ScenarioHasil2' :  ScenarioHasil2,'ScenarioHasil3' :  ScenarioHasil3})
            
        elif ScenarioH.postscenarioidno==x1 :
            Nama = projectlist.objects.filter(no=pk)
            ScenarioHasil1= scenariolist.objects.filter(projectno_id=pk).exclude(postscenarioidyes=x1).exclude(postscenarioidno=x2).exclude(postscenarioidyes=x2).exclude(scenarioid__gt=x2)
            ScenarioHasil= scenariolist.objects.filter(projectno_id=pk).exclude(postscenarioidno=x1).exclude(postscenarioidno=x2).exclude(postscenarioidyes=x2)
            ScenarioHasil2= scenariolist.objects.filter(projectno_id=pk).exclude(postscenarioidyes=x2).exclude(postscenarioidyes=x1)
            ScenarioHasil3= scenariolist.objects.filter(projectno_id=pk).exclude(postscenarioidno=x2).exclude(postscenarioidyes=x1)
            return render(request,'BPMN.html',{'ScenarioHasil':ScenarioHasil, 'ScenarioHasil1' :  ScenarioHasil1, 'Nama' : Nama 
        ,'ScenarioHasil2' :  ScenarioHasil2,'ScenarioHasil3' :  ScenarioHasil3})
        else:
            Nama = projectlist.objects.filter(no=pk)
            ScenarioHasil1= scenariolist.objects.filter(projectno_id=pk).exclude(postscenarioidyes=x1).exclude(postscenarioidno=x2)
            ScenarioHasil= scenariolist.objects.filter(projectno_id=pk).exclude(postscenarioidno=x1).exclude(postscenarioidno=x2).exclude(postscenarioidyes=x2).exclude(scenarioid__gt=x2)
            ScenarioHasil2= scenariolist.objects.filter(projectno_id=pk).exclude(postscenarioidyes=x2).exclude(postscenarioidyes=x1)
            
            return render(request,'BPMN.html',{'ScenarioHasil':ScenarioHasil, 'ScenarioHasil1' :  ScenarioHasil1, 'Nama' : Nama 
        ,'ScenarioHasil2' :  ScenarioHasil2})   
    else:
        Nama = projectlist.objects.filter(no=pk)
        return render(request,'BPMN.html',{'ScenarioHasil':scenariodisplay, 'Nama' : Nama})
