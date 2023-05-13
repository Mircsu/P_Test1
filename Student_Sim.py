import random
class Student :
        def __init__(self,name):
            self.name=name
            self.radist=1
            self.progres=1
            self.life=True

        def study(self):
            print("Let`s Go Study!")
            self.progres+=1
            self.radist-=0.5
        def chill(self):
            print("Time To Chill")
            self.prodres-=0.5
            self.radist+=1
        def sleep (self):
             print("Time go bed")
            self.radist+=1
        def proverka(self):
        if(self.progres<0):
            print("You Are Stupid! Your Die")
            self.life=False
        elif(self.radist<0):
            print("Depression Dead")
            self.life=False
        def dayoff(self):
            print("Your happynes =", self.radist)
            print("Your progres =", self.progres)
        def simulate(self,day):
            day=day
            rnd=random.randint(1,3)
            if(rnd==1):
                self.study()
            if(rnd==2):
                self,chill()
            if(rnd==3):
                self.sleep()
                self.proverka()
                self.dayoff()
ivan=Student(name="Dima")
for day in range(7):
    ivan.simulate(day)
    if(ivan.life==False):
        break

