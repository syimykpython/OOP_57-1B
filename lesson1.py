class Car:
    def __init__(self,max_speed,color,model): #init оно важно для опп, a self помогает в опредилению
        self.max_speed = max_speed
        self.color = color
        self.model = model

car_toyota = Car(160,"silver","2022")
car_honda = Car (180,"black", "2022")

print(car_honda.max_speed, car_honda.color,car_honda.model)
print(car_toyota.max_speed, car_toyota)
