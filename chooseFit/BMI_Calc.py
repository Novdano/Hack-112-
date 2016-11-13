
def getBMI(self):
    weightInKg = 0.453592*self.weight   # convert pound to kg
    heightInCm = 2.54*self.height       # inch to cm
    BMI = self.weight/(self.height/100)
    return BMI





