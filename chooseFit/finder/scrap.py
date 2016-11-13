from User import *

user1 = User(name="Justinus", age = 20, weight=150, height = 73, goal= "bulking", time=10)
user2 = User(name="Kevin", age = 18, weight=150, height =66 , goal= "slimming", time=7)

print(user1.compatibility(user2))

def getTop3(percentDict):
    listPercent = []
    for val in percentDict:
        listPercent += [val]
    listPercent.remove(100.0)
    listPercent.sort()
    print(listPercent)
    listPercent = listPercent[::-1]
    threeListInt = []
    threeList = []
    for index in range(0,5):
        percent = listPercent[index]
        threeList += [percent]
        threeListInt +=[int(percent)]
    return (threeListInt)


x = {13: "minji", 24:"gabby", 56:"proit", 90:"oiwefp", 0: "iweidf", 13:"fknsd", 100.0:"own"}

print(getTop3(x))
