



class Grendpa:
    glaz ="Grey"
    def __init__(self, glaza):
            self.glaza = glaza
    def printing(self):
            print(f"Дідусь має {dad.glaz} очі")


class dad(Grendpa):
    def __init__(self, hear):
        self.hear = hear

    def printing(self):
        print(f"Тато має {dad.glaz} очі і {self.hear} волосся")

class Son(dad):
    def __init__(self, hear):
        self.hear = hear

    def printing(self):
        print(f"Я маю {self.hear} волосся")

a=Son("brown")
a.printing()
a=dad("brown")
a.printing()