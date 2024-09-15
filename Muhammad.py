# task 1
# class Employee:
#     def __init__(self, name, salary, id):
#         self.name = name
#         self._salary = salary
#         self.__id = id

#     def show(self):
#         if self.__id == 2211:
#             print(f"{self.name} {self._salary} {self.__id}")
#         else:
#             print("EROR")
# obj = Employee("Muhammad",20000,int(input()))
# obj.show()

# name ро хама истифода бурда метонад _Salary ро факат худаш ва Class хои дарунаш истифода бурда  метонад __id ро факат худаш истифода бурда метноад тамом ва уро танхо худаш нишондода метонад



# Task 2
# class BankAkaunt:
#     def __init__(self,balans,pin):
#         self._balans = balans
#         self.__pin = pin
#     def show(self):
#         if self.__pin == 2211:
#             print(f"Your balans is {self._balans}")
#         else:
#             print("EROR")





# task 3

# class BankAkaunt:
#     def __init__(self,balans,pin):
#         self._balans = balans
#         self.__pin = pin
#     def __getstate__(self) -> object:
#         pass
#     def show(self):
#         if self.__pin == 2211:
#             print(f"Your balans is {self._balans}")
#         else:
#             print("EROR")


# task 4

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print("Animal sound!")

# class Dog(Animal):
#     def speak(self):
#         print("Puppy")

# dog = Dog("")

# dog.speak()  



# task 5

# class Person:
#     def __init__(self,name,country,date):
#         self.name = name
#         self.country = country
#         self.date = date
#     def show(self):
#         print(f"Your name is {self.name}")
#         print(f"you are from {self.country}")
#         print(f"your date birthday is {self.date}")
#         print(f"your age is {2024 - self.date}")

# person =Person("Muhammad","TAJIKISTAN",2008)
# person.show()

      
# task 7

# def get(word):
#     if word.isupper():
#         return "upper"
#     elif word.islower():
#         return "lower"
#     else:
#         return "mixed"


# print(get("whisper"))  
# print(get("SHOUT"))      
# print(get("Hello"))  


# task  9

for i in range(1, 10):
    if i <= 5:
        print((str(i) + ' ') * i)
    else:
        print((str(i) + ' ') * (10 - i))
   

