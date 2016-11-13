from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from user import *

from .models import *

class HomePage(View):
    def get(self, request):
        context = {}
        context["posts"] = userData.objects.all()[::-1]
        return render(request, 'specsForm.html', context)
        
class MakePost(View):
    def post(self, request):
        name = request.POST.get("Name")
        age = request.POST.get("Age")
        weight = request.POST.get("Weight")
        Height_Feet = request.POST.get("Height (Feet)")
        Height_Inches = request.POST.get("Height (Inches)")
        timeCommitment = request.POST.get("Time Commitment")
        #Introduction = request.POST.get("Introduction")
        Goal = request.POST.get("Goal")
        new_post = userData(name= name, age = age, weight = weight,
                     heightFeet = Height_Feet, timeCommit = timeCommitment, goals =Goal, heightInches = Height_Inches)
        new_post.save()
        return HttpResponseRedirect("/")

def dictionaryOfRecommended(user1, userList):
    

def recommended(request):
    userTested = userData.objects.all()[-1]
    userObjectList = userData.objects.all()[:-1]
    recommended = dictionaryOfRecommended(userTested, userObjectList)

    context = {}
    context["posts"] = userData.objects.all()[::-1]
    return render(request, 'recommended.html', context)
        
