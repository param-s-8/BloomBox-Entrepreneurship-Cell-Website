from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import  User,auth
from .models import Events,EventRegistrations,EventRegistrationsHackathon,Campus,Message
from datetime import datetime
#from tablib import Dataset
#from .resources import EventRegistrationsResource,EventRegistrationsHackathonResource

# Create your views here.
def index(request):
    return render(request,"index.html")

def campus(request):
    companies=Campus.objects.all()
    context={'companies':companies}
    return render(request,"campus-companies.html",context)

def events(request):
    events=Events.objects.all().order_by("-date")
    context={'events':events,'registered':False}
    return render(request,'events.html',context)

def registration(request,event):
    if request.method=="POST":
        '''form=EventRegistrationsForm(request.POST)
        if form.is_valid():
            form.save()'''
        eve=Events.objects.get(title=event)
        if eve.eventType=="Hackathon":
            leaderName=request.POST["leaderName"]
            leaderEmail=request.POST["leaderEmail"]
            leaderContact=request.POST["leaderContact"]
            college=request.POST["Hcollege"]
            noOfMembers=request.POST["noOfMembers"]
            nameOfMembers=request.POST["nameOfMembers"]
            var=EventRegistrationsHackathon.objects.create(title=eve,leaderName=leaderName,leaderEmail=leaderEmail,leaderContact=leaderContact,college=college,noOfMembers=noOfMembers,nameOfMembers=nameOfMembers)
            var.save()
            name=leaderName
        else:
            name=request.POST["name"]
            email=request.POST["email"]
            contact=request.POST["contact"]
            college=request.POST["college"]
            branch=request.POST["branch"]
            var=EventRegistrations.objects.create(title=eve,name=name,email=email,contact=contact,college=college,branch=branch)
            var.save()
        '''eventlist=Events.objects.exclude(title=event)
        activeEvents=[eve for eve in eventlist if eve.is_active()]
        print(activeEvents)
        return render(request,"thankyou.html",{'events':activeEvents,'registeredEvent':event,'name':name})'''
        events=Events.objects.all().order_by("-date")
        context={'events':events,'registered':True,'registeredEvent':event,'name':name}
        return render(request,'events.html',context)
    else:
        if Events.objects.get(title=event).is_active():
            eve=Events.objects.get(title=event)
            return render(request,'registration.html',{'event':eve})

def partners(request):
    return render(request,'sponsors.html')
        

def team(request):
    '''team20=Team.objects.filter(year=2020)
    team19=Team.objects.filter(year=2019)
    team18=Team.objects.filter(year=2018)
    team17=Team.objects.filter(year=2017)
    team16=Team.objects.filter(year=2016)
    team15=Team.objects.filter(year=2015)
    team14=Team.objects.filter(year=2014)
    team13=Team.objects.filter(year=2013)
    team12=Team.objects.filter(year=2012)
    context={'team20':team20,'team19':team19,'team18':team18,'team17':team17,'team16':team16,'team15':team15,'team14':team14,'team13':team13,'team12':team12}'''
    return render(request,'team.html')

def about(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        contact=request.POST["number"]
        message=request.POST["textarea"]
        var2=Message.objects.create(name=name,email=email,contact=contact,message=message)
    return render(request,'about.html')

'''def importcsv(request):
    file_format = "CSV"
    EventRegistrations_resource = EventRegistrationsResource()
    EventRegistrationsHackathon_resource=EventRegistrationsHackathonResource()
    dataset = EventRegistrations_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'
    return response   
    return redirect("index")'''