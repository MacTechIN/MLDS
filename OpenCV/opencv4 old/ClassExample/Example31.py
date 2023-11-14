

class Parent:
    num = 0

    def __init__(self, num):
        self.num = num
        print("The constructor of the parent class has been called")


class Child(Parent):
    def __init__(self,num):
        super().__init__(NUM)
        print("The Constructore of the child class ahs been called")

    def Display(self):
        print("num: ", self.num)




cd = Child(20)

cd.Display()