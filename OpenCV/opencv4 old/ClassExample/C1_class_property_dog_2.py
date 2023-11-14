
# Property 활용

# 데코레이터 '@property , @name.setter
# @property : 속성으로 선언
# @name.setter : name 은 @property 에 선언 되어있는 메소드 이름




#%%
class Dog:
    def __init__(self):
        self.__ownersname = 'default name'

    @property
    def name(self): # Getter
        return self.__ownersname
    @name.setter
    def name(self, name):
        self.__ownersname = name





#%%
myDog = Dog()
print(myDog.name)
print(myDog.name)

#%%
myDog.name = "Marry" # Dog.name() setter 호출
print(myDog.name) # Dog.name() getter 호출

#%%

# myDog.name('길동')
# print(myDog.set_name("name"))

