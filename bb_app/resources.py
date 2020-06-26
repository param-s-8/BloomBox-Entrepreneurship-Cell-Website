'''from import_export import resources
from .models import EventRegistrations,EventRegistrationsHackathon

class EventRegistrationsResource(resources.ModelResource):
    class Meta:
        model = EventRegistrations

class EventRegistrationsHackathonResource(resources.ModelResource):
    class Meta:
        model = EventRegistrationsHackathon
'''