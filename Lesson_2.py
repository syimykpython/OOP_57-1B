class Car:
    def __init__(self,max_speed,color,model): #init оно важно для опп, a self помогает в опредилению
        self.max_speed = max_speed
        self.color = color
        self.model = model

def drive_to_lokation(self, location):
    print(f'car {self.model} is driving to {location}')

car_honda = Car(160, "silver", "Honda_fit")
car_toyota = Car(180,"black","toyota_camry_m5")
print(car_honda.max_speed,car_honda.color, car_honda.model)
print(car_toyota.max_speed,car_toyota.color,car_toyota.model)