from django.shortcuts import render,redirect
from app.models import projectlist
from app.forms import projectform
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
