
# Property 활용
class Dog:
    def __init__(self):  # 생성자
    self.__ownersname = 'default name'

    def get_name(self): # Getter
        return self.__ownersname

    def set_name(self, name):
        self.__ownersname = name

    name = "default"
    gender = 'Male/Female'
    ownernames = 'default name'


    def Bark(self):
        print(self.name + ': 멍멍')

dog1 = Dog()

dog1.name = '멍멍이'
dog1.gender ='Female'
dog1.ownernames ='Sam'


dog1.Bark()


