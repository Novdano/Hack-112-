import random
import math
import googlemaps

class Excercise (object):
	def __init__(self, name, muscleGroup = None, link = None):
		self.name = name
		self.muscleGroup = muscleGroup

	def __hash__(self):
		attributes = (self.name, self.muscleGroup)
		return hash(attributes)

def getBulkExercises():
	BP = Excercise ("Bench Press", muscleGroup = "Chest", link = "https://www.youtube.com/watch?v=6JtP6ju0IMw")
	SP = Excercise ("Shoulder Press", muscleGroup = "Shoulders", link = "https://www.youtube.com/watch?v=qEwKCR5JCog")
	F = Excercise ("Fly", muscleGroup = "Chest", link = "https://www.youtube.com/watch?v=_4JjOqy0UiY")
	HC = Excercise ("Hammer Curls", muscleGroup = "Biceps", link = "https://www.youtube.com/watch?v=IOOU5yChBhk")
	TP = Excercise ("Tricep Pushdown", muscleGroup = "Tricep", link = "https://www.youtube.com/watch?v=BLvSbziilmo")
	LP = Excercise ("Leg Press", muscleGroup = "Legs", link = "https://www.youtube.com/watch?v=Aq5uxXrXq7c")

	bulkExercises = [BP, SP, F, HC, TP, LP]
	return bulkExercises

def getCardioExercises():
	Jog = Excercise ("Jog", link = "https://www.youtube.com/watch?v=C0rS43ocutI")
	BW = Excercise ("Brisk Walk", link = "https://www.youtube.com/watch?v=YLZhIQwt6L8")
	HIIT = Excercise("HIIT", link = "https://www.youtube.com/watch?v=tbbZBtdd20U")
	CT = Excercise ("Circuit Training", link = "https://www.youtube.com/watch?v=460nSW7xEok")
	Rowing = Excercise ("Rowing", link = "https://www.youtube.com/watch?v=bc2bVqkkcDE")
	Zumba = Excercise ("Zumba", link = "https://www.youtube.com/watch?v=HRkNfdlm5Qs")
	
	cardioExercises = [Jog, BW, HIIT, CT, Rowing, Zumba]
	return cardioExercises

class User (object):

	bulkExercises = getBulkExercises()
	cardioExercises = getCardioExercises()
	gmaps = googlemaps.Client(key = "AIzaSyA0xMFw7tA4Oq8tWnArYl5nkFPiJ-qw6Vo")

	def __init__(self, name = None, age = None, weight = None, height = None, 
				goal = None, time = None, address = "", city = "", state = ""):
		self.name = name
		self.age = age
		self.weight = weight
		self.height = height
		self.goal = goal
		self.time = time
		self.location = self.getLocationString(address, city, state)
		self.BMI = self.getBMI()
		assert(goal == None or goal == "health" or 
									goal == "bulking" or goal == "slimming")
		if(self.goal == None or self.goal == "health"):
			if(self.BMI < 18.5): self.goal == "bulking"
			elif(18.5 <= self.BMI <= 24.9): self.goal = "midrange"
			elif(self.BMI > 24.9): self.goal = "slimming"
		self.recommendations = self.getRecommendations()

	def compatibility(self, other):
		if(not isinstance(other, User)): return 0
		compatibility = 100
		multipliers = 0
		multiplierSum = 0

		#comparing goals
		if ((self.goal == "slimming" and other.goal == "bulking") or 
			 (self.goal == "bulking" and other.goal == "slimming")):
			compatibility -= 30
		elif(self.goal != other.goal): compatibility -= 10

		#comparing BMI
		BMIDifference = abs(self.BMI - other.BMI)
		BMIBase = 1.083088307
		BMIMultiplier = BMIBase**(-BMIDifference) #exponential decay
		multiplierSum += BMIMultiplier
		multipliers += 1

		#comparing distance
		distance = self.getDistance(other)
		if(distance != None):
			multiplierBase = 1/.95
			distanceMultiplier = multiplierBase**(-distance)
			multiplierSum += distanceMultiplier
			multipliers += 1

		#comparing time commitment
		if(self.time != None and other.time != None):
			if(self.time == 0 or other.time == 0): return 0
			timeMultiplier = 1 - abs(math.log(self.time) 
														- math.log(other.time))
			timeMultiplier = max(0, timeMultiplier)
			multiplierSum += timeMultiplier
			multipliers += 1

		multiplier = multiplierSum/multipliers
		compatibility *= multiplier
		compatibility = compatibility//.1/10 #format the compatibility number
		return (compatibility, distance)

	def getDistance(self, other):
		try:
			matrix = User.gmaps.distance_matrix(self.location, other.location)
		except:
			return None
		destinationInfo = matrix["rows"][0]["elements"][0]
		if (destinationInfo["status"] != "OK"): return None
		distanceM = destinationInfo["distance"]["value"]
		distanceMi = distanceM/1609.34 #convert from meters to miles
		formattedDistance = distanceMi//.1/10
		return formattedDistance

	def getBMI(self):
		if(self.height == None or self.weight == None): return 0
		if(self.height <= 0): return 0
		weightInKg = 0.453592*self.weight
		heightInM = .0254*self.height       # inch to cm
		BMI = weightInKg/(heightInM**2)
		return BMI

	def getLocationString(self, address, city, state):
		location = address
		if(location != ""): location += ", " + city
		else: location = city
		if(location != ""): location += ", " + state
		else: location = state
		return location

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

	def __hash__(self):
		attributes = (self.name, self.age, self.weight, self.height, self.goal)
		return hash(attributes)

'''
test = User(name = "Eric", age = 19, weight = 120, height = 67)
test2 = User(name = "Nov", age = 19, weight = 140, height = 72)
test3 = User(name = "Rishabh", age = 18, weight = 154, height = 70)
'''