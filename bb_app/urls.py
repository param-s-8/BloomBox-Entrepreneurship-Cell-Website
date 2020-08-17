from django.urls import path
from . import views,urls
from django.conf import settings


urlpatterns = [
    path('', views.index,name="index"),
    path('index.html', views.index,name="index"),
    path('campus',views.campus,name="campus"),
    path('events',views.events,name="events"),
    path('registration/<str:event>',views.registration,name="registration"),
    path('partners',views.partners,name="partners"),
    path('team',views.team,name="team"),
    path('about',views.about,name="about"),
    path('results',views.results,name="results"),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)