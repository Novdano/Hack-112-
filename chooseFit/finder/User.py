import random
import math
#photo = PhotoImage(file = "images.png")

class Excercise (object):
	def __init__(self, name, muscleGroup = None):
		self.name = name
		self.muscleGroup = muscleGroup

	def __repr__(self):
		return self.name

	def __hash__(self):
		attributes = (self.name, self.muscleGroup)
		return hash(attributes)

def getBulkExercises():
	BP = Excercise ("Bench Press", "Chest")
	SP = Excercise ("Shoulder Press", "Shoulders")
	F = Excercise ("Fly", "Chest")
	HC = Excercise ("Hammer Curls", "Biceps")
	TP = Excercise ("Tricep Pushdown", "Tricep")
	LP = Excercise ("Leg Press", "Legs")

	bulkExercises = [BP, SP, F, HC, TP, LP]
	return bulkExercises

def getCardioExercises():
    cardioExercises = []
    exercises = [
                      'Jog', 'Brisk Walk', 'HIIT',
                      'Circuit Training', 'Rowing', 'Zumba'
                ]

    for exercise in exercises:
        cardioExercises.append(Excercise(exercise))
    return cardioExercises

class User (object):

	bulkExercises = getBulkExercises()
	cardioExercises = getCardioExercises()

	def __init__(self, name = None, age = None, weight = None, height = None, 
													goal = None, time = None):
		self.name = name
		self.age = age
		self.weight = weight
		self.height = height
		self.goal = goal
		self.time = time
		self.BMI = self.getBMI()
		if(self.goal == None or self.goal == "health"):
			if(self.BMI < 18.5): self.goal == "bulking"
			elif(18.5 <= self.BMI <= 24.9): self.goal = "midrange"
			elif(self.BMI > 24.9): self.goal = "slimming"
		self.recommendations = self.getRecommendations()

	def getBMI(self):
	    weightInKg = 0.453592*self.weight   # convert pound to kg
	    heightInM = .0254*self.height       # inch to cm
	    BMI = weightInKg/(heightInM**2)
	    return BMI

	def getMidRangeExercises(self):
	    # mid range 18.5 - 24.9
	    # perf = 21.7
	    numberOfExercises = 6
	    CategoryRange = (25.0-18.5)/numberOfExercises
	    numberOfCardio = (self.BMI - 18.5)//CategoryRange + 1
	    numberOfBulk = numberOfExercises - numberOfCardio
	    exercises = []
	    while len(exercises) < numberOfCardio:
	    	exercise = random.choice(User.cardioExercises)
	    	if(not exercise in exercises): exercises.append(exercise)
	    while len(exercises) < numberOfExercises:
	    	exercise = random.choice(User.bulkExercises)
	    	if(not exercise in exercises): exercises.append(exercise)
	    return exercises 

	def getRecommendations(self):
		if(self.goal == "bulking"): return User.bulkExercises
		elif(self.goal == "slimming"): return User.cardioExercises
		else: return self.getMidRangeExercises()

	def compatibility(self, other):
		if(not isinstance(other, User)): return None

		compatibility = 100
		if (self.goal != other.goal):
			compatibility -= 30
		BMICompatability = 1 - abs(self.BMI - other.BMI)/10
		BMICompatability = max(0, BMICompatability)
		compatibility *= BMICompatability
		if(self.time != None and other.time != None):
			timeCompatability = 1 - abs(math.log(self.time) 
														- math.log(other.time))
			timeCompatability = max(0, timeCompatability)
			compatibility *= timeCompatability
		return compatibility	

	def __hash__(self):
		attributes = (self.name, self.age, self.weight, self.height, self.goal)
		return hash(attributes)

'''
test = User(name = "Eric", age = 19, weight = 120, height = 67)
test2 = User(name = "Nov", age = 19, weight = 140, height = 72)
test3 = User(name = "Rishabh", age = 18, weight = 154, height = 70)
'''