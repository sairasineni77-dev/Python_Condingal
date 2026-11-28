class student:
    grade = 10
    print("Hi I am a student of grade", grade)

ob = student()

class Vehicle:
    def __init__(self, max_speed_1, mileage_1):

        self.max_speed = max_speed_1
        self.mileage = mileage_1

modelX = Vehicle(240,18)

print("Model Max Speed:", modelX.max_speed)
print("Model Mileage:", modelX.mileage)
        