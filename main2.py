# Вложенный цикл
# myList = [[1, 3, 2, 4], [1, 8, 6], [9, 4, 6]]

# for i in myList:
#     for j in i:
#         print(j)

# value = int(input('Enter a number: '))
# result = 10 / value 
# print(f'result: {result}')

# try:
#     value = int(input('Enter a number: '))
#     result = 10 / value 
# except ValueError:
#     print('Вы ввели не число!')
# except ZeroDivisionError:
#     print('На ноль делить нельзя!')
# else:
#     print(f'Результат: {result}')
# finally: 
#     print('Выполнится в любом случае!')

# print('Дальнейшая работа кода...')
# ZeroDivisionError
# ValueError 

# number = 12.5437898765567654
# print(number)
# print(round(number, 2)) - округляет до двуз чисел после знака
# print(round(number)) - окургляет просто 

# import math

# num = 2.3
# round_num = math.ceil(num) - округляется до большего значения
# print(round_num)

# print(type ('hello'))


# class Person: 
#     name = 'Sten'

# p1 = Person()
# p1.name = 'John'
# print(p1.name)

# p2 = Person
# print(p2.name)

# class Person: 
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age - функции внутри класса это методы 
    
#     def myFunc(self):
#         print('hello, my name is ' + self.name)

#     def ageUp(self)
# p1 = Person('John', 36)
# p1.age = 40
# print(p1.age)


class Player: 
    def __init__(self, strenght: int, speed: int, name: str, carryWeight: int):
        self.strenght = strenght
        self.speed = speed 
        self.name = name
        self.carryWeight = carryWeight 

    def speedUp(self):
        self.speed *= 2

p1 = Player(10, 5, 'John', 20)
print(p1.name, p1.strenght, p1.speed, p1.carryWeight)
p1.speedUp()
print(p1.speed)
