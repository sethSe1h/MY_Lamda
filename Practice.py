# from functools import reduce
# x = lambda a,b,c: a + b + c
# print(x(2,3,4))
# check = lambda a,b: "Is equal" if a == b else "Isn't equal"
# print(check(5,5))
# my_list = [1,2,3,5,2,7,9,10]
# even = filter(lambda x: x % 2 == 0, my_list)
# odd = filter(lambda  x: x % 2 != 0, my_list)
# print(list(even))
# print(list(odd))
# plus = reduce(lambda x, y: x + y, my_list)
# print(plus)
# mul = map(lambda x: x * 2, my_list)
# print(list(mul))
# cal = lambda x, y: (x + y, x * y)
# print(cal(3,4))

#Tuple
# myTuple = ("William", "Boromey", "Piseth")
# myIter = iter(myTuple)
# for i in myIter:
#     print(i)

#Module
# import platform
# x = platform.system()
# print(x)
# x = dir(platform)
# print(x)

#Global scope
# def printf():
#     global x
#     x = lambda x, y: (x + y, x * y)
#     print(x(5,4))
# printf()

#Datetime
# import datetime
# x = datetime.date.today()
# print(x)

#Math
# import math
# x = math.pi
# print(x)
# print(pow(5,3))

#Json
# import json
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# y = json.loads(x)
# print(y["name"])
# x = {"name": "John",
#      "age": 30,
#      "city": "New York"}
# y = json.dumps(x)
# print(y)

# def f(x):
#   if x % 2== 0:
#     return True
#   else:
#     return False
#
#
# def is_divisible(number, divisor):
#   return number % divisor == 0
#
# def is_even(number):
#   return is_divisible(number, 2)
# print(f(3))
# print(is_even(6))

# def board_in_word(words: str):
#   max_length = max(len(word) for word in words)
#   board = "*" * (max_length + 4)
#   print(board)
#   for word in words:
#     print(f"* {word.ljust(max_length)} *")
#   print(board)
# word_list = ["Hello", "World", "in", "a", "frame"]
# board_in_word(word_list)


