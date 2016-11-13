from User import *

user1 = User(name="Justinus", age = 20, weight=150, height = 73, goal= "bulking", time=10)
user2 = User(name="Kevin", age = 18, weight=150, height =66 , goal= "slimming", time=7)

print(user1.compatibility(user2))