from django.shortcuts import render
from accounts.views import *

def dashboard(request):
   list_users()
   return render(request,'dashboard/index.html', context={})
