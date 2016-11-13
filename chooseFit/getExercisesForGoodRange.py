def getExercises(BMI):
    # mid range 18.5 - 24.9
    # perf = 21.7
    bulking = []
    cardio = []
    if(18.5 <= BMI <= 19.57):
        for i in range(5):
            bulking.append(random.choice(bulkingExercises))
        cardio.append(random.choice(cardioExercises))
    elif(19.58 <= BMI <= 20.64):
        for i in range(4):
            bulking.append(random.choice(bulkingExercises))
        for j in range(2):
            cardio.append(random.choice(cardioExercises))
    elif(20.65 <= BMI <= 22.76):
        for i in range(3):
            bulking.append(random.choice(bulkingExercises))
            cardio.append(random.choice(cardioExercises))
    elif( 22.77 <= BMI <= 23.83):
        for i in range(2):
            bulking.append(random.choice(bulkingExercises))
        for j in range(4):
            cardio.append(random.choice(cardioExercises))
    elif(22.84 <= BMI <= 24.9):
        bulking.append(random.choice(bulkingExercises))
        for j in range(5):
            cardio.append(random.choice(cardioExercises))
    return(bulking, cardio)   
