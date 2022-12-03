from django.shortcuts import render
from .models import Starthome, Startteam, Startportfolio, Startme

def Indexview(request):
    
    starthome=Starthome.objects.all()
    startteam=Startteam.objects.all()
    startme=Startme.objects.all()
    startportfolio=Startportfolio.objects.all()
    context={
                'starthome':starthome, 
                'startteam':startteam,
                "startportfolio":startportfolio,
                'startme':startme
                   
                }
    
    return render(request,'index.html', context=context )
