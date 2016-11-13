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
        introduction = request.POST.get("Introduction")
        location = request.POST.get("Location")
        city = request.POST.get("City")
        state = request.POST.get("State")
        Goal = request.POST.get("Goal")
        new_post = userData(name= name, age = age, weight = weight,
                     heightFeet = Height_Feet, timeCommit = timeCommitment,
                      intro = introduction, goals =Goal, heightInches = Height_Inches, 
                      location = location, city = city, state = state)
        new_post.save()
        return HttpResponseRedirect("/recommended")

#return only the compatibility without the tuple
def dictionaryOfRecommended(user1, userList):
    recomm = dict()
    for userObjects in userList:
        heightUser = height(userObjects.heightFeet, userObjects.heightInches)
        user = User(name = userObjects.name, age = userObjects.age, 
                        weight = userObjects.weight, height=heightUser, 
                        goal = userObjects.goals, time = userObjects.timeCommit, 
                        address =userObjects.location, city = userObjects.city, state = userObjects.state)
        compatibility = (user1.compatibility(user))[0]
        distance = (user1.compatibility(user))[1]
        recomm[compatibility] = (userObjects.name, distance)
    return recomm

def getTop5(percentDict):
    listPercent = []
    for val in percentDict:
        listPercent += [val]
    listPercent.remove(99.9)
    listPercent.sort()
    listPercent = listPercent[::-1]
    fiveListInt = []
    fiveList = []
    for index in range(0,5):
        percent = listPercent[index]
        fiveList += [percent]
        fiveListInt +=[int(percent)]
    names = [percentDict[fiveList[0]][0], percentDict[fiveList[1]][0], 
                percentDict[fiveList[2]][0], percentDict[fiveList[3]][0], 
                percentDict[fiveList[4]][0]]
    distance = [percentDict[fiveList[0]][1], percentDict[fiveList[1]][1], 
                percentDict[fiveList[2]][1], percentDict[fiveList[3]][1], 
                percentDict[fiveList[4]][1]]
    user1 = userData.objects.get(name = names[0])
    user2 = userData.objects.get(name = names[1])
    user3 = userData.objects.get(name = names[2])
    user4 = userData.objects.get(name = names[3])
    user5 = userData.objects.get(name = names[4])
    name = [user1, user2, user3, user4, user5]
    return (name, distance, fiveListInt) #name is the userData object from the database

def height(heightFeet, heightInches):
    return heightFeet*12 + heightInches

def recommended(request):
    userTestedObject = userData.objects.last()
    userObjectList = userData.objects.all()
    heightUserTested = height(userTestedObject.heightFeet, userTestedObject.heightInches)
    userTested = User(name = userTestedObject.name, age = userTestedObject.age, 
                        weight = userTestedObject.weight, height=heightUserTested, 
                        goal = userTestedObject.goals, time = userTestedObject.timeCommit,
                        address = userTestedObject.location, city = userTestedObject.city, 
                        state = userTestedObject.state)
    #return the list of people, distance and compatibility
    compatibilityDict = dictionaryOfRecommended(userTested, userObjectList)
    recommendedList, distanceList, compatibilityList = (getTop5(compatibilityDict)[0], 
                                    getTop5(compatibilityDict)[1],
                                    getTop5(compatibilityDict)[2])
    #return the list of recommended exercises
    exercises = userTested.getRecommendations()
    #return the distance from each other
    context = {"analyzed": userTestedObject,
                "users": recommendedList,
                "compatibilities": compatibilityList,
                "index": [0,1,2,3,4],
                "exercises": exercises,
                "distance": distanceList,
                }
    return render(request, 'recommended.html', context)

def partnerProfile(request, id):
    user = get_object_or_404(userData, id=id)
    context = {
        "title": user.name,
        "object": user, 
    }
    return render(request, "profile.html", context)
        
