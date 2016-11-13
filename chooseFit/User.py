class User (object):

	def __init__(self, name = None, age = None, weight = None, height = None, goal = None, time = None):
		self.name = name
		self.age = age
		self.weight = weight
		self.height = height
		self.goal = goal
		self.time = time
		self.BMI = self.getBMI()
		if(self.goal == None or self.goal == "health"):
			if(self.BMI < 18.5): self.goal == "bulk"
			elif(18.5 <= self.BMI <= 24.9): self.goal = "midrange"
			elif(self.BMI > 24.9): self.goal = "cut"

	def getBMI(self):
	    weightInKg = 0.453592*self.weight   # convert pound to kg
	    heightInM = .0254*self.height       # inch to cm
	    print(weightInKg)
	    BMI = weightInKg/(heightInM**2)
	    return BMI

	def getRecommendations(self):
		pass

class Excercise (object):
	def __init__(self, name, goal, muscleGroup = None):
		self.name = name
		self.goal = goal
		self.muscleGroup = muscleGroup

test = User(name = "Eric", age = 19, weight = 120, height = 67)