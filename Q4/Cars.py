class Vehicle:
    count=0
    cars=[]
    def __init__(self,_type,_mark,_wheels):
        self.type=_type
        self.mark=_mark
        self.wheels=_wheels
        Vehicle.count+=1
        Vehicle.cars.append(self)

    def drive(self,distance,speed=60):
        print("Drive {0} Km with speed {1} Km/h".format(distance,speed))

    def printCarsDetails():
        print("Total Number of cars",Vehicle.count)
        for c in Vehicle.cars:
            c.print()

class Car(Vehicle):
    def __init__(self,_type,_mark,_wheels,_fuel_capacity=100):
        Vehicle.__init__(self,_type,_mark,_wheels)
        self.fuel_capacity=_fuel_capacity
        self.fuel_level=_fuel_capacity

    def drive(self,distance,speed=60):
        if speed<100:
            fuel=distance/4
        else:
            fuel=distance/2
        if fuel>self.fuel_level:
            print("Can't drive {0} Km no enough fuel!".format(distance))
        else:
            Vehicle.drive(self,distance,speed)
            self.fuel_level-=fuel
            print("The remaining fuel: {0} L".format(self.fuel_level))

    def fill(self):
        fuel=self.fuel_capacity-self.fuel_level
        self.fuel_level=self.fuel_capacity
        print("fill the Car with {0} L of fuel".format(fuel))

    def print(self):
        print("Type: {0}, Mark: {1}, Wheels: {2}, Capacity: {3}, Fuel: {4}".format(self.type,self.mark,self.wheels,self.fuel_capacity,self.fuel_level))

class ElectricCar(Vehicle):
    def __init__(self,_type,_mark,_wheels):
        Vehicle.__init__(self,_type,_mark,_wheels)
        self.battery_level=100

    def drive(self,distance,speed=60):
        if speed<100:
            battery=distance/4
        else:
            battery=distance/2
        if battery>self.battery_level:
            print("Can't drive {0} Km no enough battery charge!".format(distance))
        else:
            Vehicle.drive(self,distance,speed)
            self.battery_level-=battery
            print("The battery charge level: {0}%".format(self.battery_level))

    def charge(self):
        self.battery_level=100
        print("The battery is fully charged")

    def print(self):
        print("Type: {0}, Mark: {1}, Wheels: {2}, Battery Level: {3}%".format(self.type,self.mark,self.wheels,self.battery_level))

c1=Car('RIO','KIA',4)
c2=Car('Corolla','Toyota',4,150)
c3=ElectricCar('Tesla','Tesla',4)

Vehicle.printCarsDetails()

print("\n\n######### First Car #########")

c1.drive(100)
c1.drive(100,120)
c1.drive(100,120)
c1.fill()
c1.drive(100,120)

print("\n\n######### Second Car #########")

c2.drive(100)
c2.drive(100,120)
c2.drive(100,120)

print("\n\n######### Third Car #########")

c3.drive(100)
c3.drive(100,120)
c3.drive(100,120)
c3.charge()
c3.drive(100,120)
     
print("\n\n#############################")
Vehicle.printCarsDetails()
