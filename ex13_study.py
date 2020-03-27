from sys import argv

age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weight? ")
like = input("What do you like? ")
script = "ex13_study.py"

argv = script, age, height, weight, like
s, a, h, w, l = argv
print("script:", s)
print("age:", a)
print("height:", h)
print("weight:", w)
print("like:", l)