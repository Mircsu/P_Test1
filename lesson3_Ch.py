class Human:
    def __init__(self,name):
        self.name=name

class Auto:
    def __init__(self,brand):
        self.brand=brand
        self.passengers=[]
    def add_passengers(self,*args):
        for passenger in args:
            self.passengers.append(passenger)
    def print_passengers(self):
        if self.passengers !=[] :
            print(f"В автомобілі {self.brand} кількість пасажирів = ")
            for passenger in self.passengers:
                print(passenger.name)
