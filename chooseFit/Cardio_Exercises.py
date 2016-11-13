
class Excercise (object):
    def __init__(self, name, goal="hi", muscleGroup = "hi"):
        self.name = name
        self.muscleGroup = muscleGroup

def getCardioExercises():
    cardioExercises = []
    exercises = [
                      'Jog', 'Brisk Walk', 'HIIT', 'Short Sprints', 
                      'Circuit Training', 'Rowing', 'Yoga', 'Stretching',
                      'Pilates', 'Zumba'
                ]

    for exercise in exercises:
        cardioExercises.append(Excercise(exercise))

    return cardioExercises



