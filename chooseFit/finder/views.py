from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from User import *

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
        return HttpResponseRedirect("/recommended")

def dictionaryOfRecommended(user1, userList):
    recomm = dict()
    for userObjects in userList:
        heightUser = height(userObjects.heightFeet, userObjects.heightInches)
        user = User(name = userObjects.name, age = userObjects.age, 
                        weight = userObjects.weight, height=heightUser, 
                        goal = userObjects.goals, time = userObjects.timeCommit)
        compatibility = user1.compatibility(user)
        recomm[compatibility] = userObjects.name
    return recomm

def getTop3(percentDict):
    listPercent = list(percentDict)
    listPercent.remove(100.0)
    listPercent = listPercent[::-1]
    threeListInt = []
    threeList = []
    for index in range(0,3):
        percent = listPercent[index]
        threeList += [percent]
        threeListInt +=[int(percent)]
    names = [percentDict[threeList[0]], percentDict[threeList[1]], 
                percentDict[threeList[2]]]
    user1 = userData.objects.get(name = names[0])
    user2 = userData.objects.get(name = names[1])
    user3 = userData.objects.get(name = names[2])
    name = [user1, user2, user3]
    return (name, threeListInt)

def height(heightFeet, heightInches):
    return heightFeet*12 + heightInches

def recommended(request):
    userTestedObject = userData.objects.last()
    userObjectList = userData.objects.all()
    heightUserTested = height(userTestedObject.heightFeet, userTestedObject.heightInches)
    userTested = User(name = userTestedObject.name, age = userTestedObject.age, 
                        weight = userTestedObject.weight, height=heightUserTested, 
                        goal = userTestedObject.goals, time = userTestedObject.timeCommit)
    compatibilityDict = dictionaryOfRecommended(userTested, userObjectList)
    recommendedList, compatibilityList = getTop3(compatibilityDict)[0], getTop3(compatibilityDict)[1]
    context = {"analyzed": userTestedObject,
                "users": recommendedList, 
                "compatibilities": compatibilityList}
    return render(request, 'recommended.html', context)
        
