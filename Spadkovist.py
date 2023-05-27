class Human:
    lasson_day="Saturday"
class Student(Human) :
    def __init__(self,dz,rating):
        self.dz=dz
        self.rating=rating
    def printing(self):
        print(f"Студент має {self.dz} просрочок та займає {self.rating} місце в рейтенгу")
class Dima(Student):
    def __init__(self,hobby):
        self.hobby=hobby
    def printing(self):
        print(f"Захопленням студента є {self.hobby} ")
class Zhenya(Human):
    def __init__(self,group,mark):
        self.group=group
        self.mark=mark
    def printing(self):
        print(f"Вчитель вкладає у групи {self.group} та поставив групі середній бал {self.mark}")
std=Dima("Комп'терні ігри")
std.printing()
artem=Student("96","998")
artem.printing()
teacher=Zhenya("С2912", "10")
teacher.printing()

