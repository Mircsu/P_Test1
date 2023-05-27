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


h1=Human("Dima")
h2=Human("Svyat")
h3=Human("Lyoha")
car1=Auto("Fiat")
car2=Auto("Toyota")
car3=Auto("Hyundai")
car4=Auto("Ford")
car1.add_passengers(h1,h2)
car2.add_passengers(h2,h3)
car3.add_passengers(h1)
car4.add_passengers(h3,h1)
car1.print_passengers()
car2.print_passengers()
car3.print_passengers()
car4.print_passengers()

