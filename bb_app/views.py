from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import  User,auth
from .models import Events,EventRegistrations,EventRegistrationsHackathon,ESummitRegistration,ESummitRegistrationHackathon,Campus,Message, ESummitMessage
from datetime import datetime
#from tablib import Dataset
#from .resources import EventRegistrationsResource,EventRegistrationsHackathonResource

# Create your views here.
def index(request):
    return render(request,"index.html")

def campus(request):
    companies=Campus.objects.all().order_by("name")
    active_companies=["Nurturing Lives","Synergy","LAUNCHiT","&Evolve","Learnation","Notebook","Pasken","Studbud","Passed On Wisdom"]
    context={'companies':companies,'active_companies':active_companies}
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
            nameOfTeam=request.POST["nameOfTeam"]
            nameOfMembers=request.POST["nameOfMembers"]
            var=EventRegistrationsHackathon.objects.create(title=eve,leaderName=leaderName,leaderEmail=leaderEmail,leaderContact=leaderContact,college=college,nameOfTeam=nameOfTeam,nameOfMembers=nameOfMembers)
            var.save()
            name=leaderName
        else:
            name=request.POST["name"]
            email=request.POST["email"]
            contact=request.POST["contact"]
            college=request.POST["college"]
            branch=request.POST["branch"]
            year=request.POST["year"]
            var=EventRegistrations.objects.create(title=eve,name=name,email=email,contact=contact,college=college,branch=branch,year=year)
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

def enspire(request):
    return render(request,'enspire.html')

def results(request):
    return render(request, 'results.html')
        

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


def ESummit(request):
    return render(request,'eSummit.html')

def ESummitRegistration(request, eventId):
    if (eventId >=1 and eventId <=7):
        eventMappings = {1:'Ennovate', 2:'Zero to Hero - A Success Story',3:'Ideathon',4:'BizQuiz',5:'Rising Entrepreneur',6:'Financial Planning in Student Life',7:'Mock Crypto Trading Contest'}
        if request.method == "POST":
            eventName = eventMappings.get(eventId)
            if(eventId in [2,6,7]):
                email=request.POST["email"]
                name=request.POST["name"]
                contact=request.POST["contact"]
                college=request.POST["college"]
                branch=request.POST["branch"]
                year=request.POST["year"]
                esummit_var=ESummitRegistration.objects.create(email=email,eventId=eventId, eventName=eventName, name=name, contact=contact, college=college, branch=branch, year=year)
                esummit_var.save()
            else:
                nameOfTeam=request.POST["nameOfTeam"]
                leaderEmail=request.POST["leaderEmail"]
                leaderName=request.POST["leaderName"]
                leaderContact=request.POST["leaderContact"]
                college=request.POST["Hcollege"]
                alternateEmail=request.POST["alternateEmail"]
                alternateContact=request.POST["alternateContact"]
                nameOfMembers=request.POST["nameOfMembers"]
                esummit_var=ESummitRegistrationHackathon.objects.create(eventId=eventId, eventName=eventName,nameOfTeam=nameOfTeam,leaderEmail=leaderEmail,leaderName=leaderName,leaderContact=leaderContact,college=college,alternateEmail=alternateEmail,alternateContact=alternateContact,nameOfMembers=nameOfMembers)
                esummit_var.save()
            return render(request,'eSummit.html')
        else:
            if(eventId in [2,6,7]):
                eventType=1
            else:
                eventType=2
            eventName = eventMappings.get(eventId)
            context={'eventId':eventId, 'eventType':eventType, 'eventName':eventName}
            return render(request, 'eSummitRegistration.html', context)
    else:
        return render(request, 'eSummit.html')


def eSummitQuery(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        contact=request.POST["number"]
        message=request.POST["textarea"]
        query_var=ESummitMessage.objects.create(name=name,email=email,contact=contact,message=message)
    return render(request,'eSummit.html')

'''def importcsv(request):
    file_format = "CSV"
    EventRegistrations_resource = EventRegistrationsResource()
    EventRegistrationsHackathon_resource=EventRegistrationsHackathonResource()
    dataset = EventRegistrations_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'
    return response   
    return redirect("index")'''