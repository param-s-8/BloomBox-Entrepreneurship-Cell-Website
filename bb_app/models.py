from django.db import models
from datetime import datetime,date    
import os,pytz
from django.utils import timezone
# Create your models here.
class Campus(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/campus-company/cc-logos',blank=True, null=True)
    students=models.TextField()
    description=models.TextField()
    def __str__(self):
        return self.name


def get_path_events(instance, filename):
        return os.path.join(
        "images/events/%s" % instance.title.title, filename)

TYPE_CHOICES = (
    ("Panel Session", "Panel Session"),
    ("Workshop", "Workshop"),
    ("Hackathon", "Hackathon"),
    ("FunLearning", "FunLearning"),
)


class Events(models.Model):
    title=models.CharField(primary_key=True,max_length=255)
    description=models.TextField()
    date=models.DateField(help_text = "Please use the following format: <em>YYYY-MM-DD</em>.")
    details=models.TextField()
    eventType=models.CharField(max_length=13, choices=TYPE_CHOICES, default="Panel Session")
    deadline=models.DateTimeField(default=datetime.now(),help_text = "Please use the following format: <em>YYYY-MM-DD</em>.")
    feedbackStatus=models.CharField(max_length=13, choices=(("Active","Active"),("Inactive","Inactive")), default="Inactive")
    def is_active(self):
        return self.deadline > timezone.now()
    def __str__(self):
        return self.title

class EventImages(models.Model):
    title=models.ForeignKey(Events,on_delete=models.CASCADE,related_name="moreImages")
    moreImages = models.ImageField(upload_to=get_path_events,blank=True, null=True)

class EventRegistrations(models.Model):
    title=models.ForeignKey(Events,on_delete=models.CASCADE,related_name="registrations")
    name=models.CharField(max_length=100)
    email=models.EmailField()
    contact=models.CharField(max_length=50)
    college=models.CharField(max_length=255,default="K. J. Somaiya College of Engineering")
    branch=models.CharField(max_length=100)
    year=models.CharField(max_length=2, default="TY")
    def __str__(self):
        return self.title + "_" + self.email
    
class EventRegistrationsHackathon(models.Model):
    title=models.ForeignKey(Events,on_delete=models.CASCADE,related_name="registrationsHackathon")
    leaderName=models.CharField(max_length=100)
    leaderEmail=models.EmailField()
    leaderContact=models.CharField(max_length=50)
    college=models.CharField(max_length=255,default="K. J. Somaiya College of Engineering")
    nameOfTeam=models.CharField(max_length=50)
    nameOfMembers=models.TextField()
    def __str__(self):
        return self.title + "_" + self.leaderEmail

def get_path_team(instance, filename):
    return os.path.join(
    "images/teams/%d" % instance.year, filename)

class Team(models.Model):
    image=models.ImageField(upload_to=get_path_team,blank=True, null=True)
    name=models.CharField(max_length=255) 
    post=models.CharField(max_length=100)
    email=models.URLField(max_length=500)
    facebook=models.URLField(max_length=500)
    linkedin=models.URLField(max_length=500)
    year=models.IntegerField(help_text="Enter in this format:2020")

class Message(models.Model):     #about us
    name=models.CharField(max_length=255)
    email=models.EmailField()
    contact=models.CharField(max_length=15)
    message=models.TextField()
    def __str__(self):
        return self.name
