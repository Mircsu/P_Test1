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
         def sleep (selp):
             print("Time go bed")
            self.radist+=1