class Human:
    lasson_day="Saturday"
class Student(Human) :
    def __init__(self,dz,rating)
        self.dz=dz
        self.rating=rating
    def printing(self):
        print(f"Студент має {self.dz} просрочок та займає {self.rating} місце в рейтенгу")
class Dima(Student):
    def __init__(self,hobby):
        self.hobby=hobby
    def printing(self):
        print(f"Захопленням студента є {self.hobby} ")
