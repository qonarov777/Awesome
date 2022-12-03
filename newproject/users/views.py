from django.shortcuts import render

def Userview(request):
    return render(request, 'users.html')
