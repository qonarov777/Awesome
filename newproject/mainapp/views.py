from django.shortcuts import render
from .models import Starthome, Startabout

def Indexview(request):
    
    starthome=Starthome.objects.all()
    startabout=Startabout.objects.all()
    context={
                'starthome':starthome, 
                'startabout': startabout,     
                }
    
    return render(request,'index.html', context=context )
