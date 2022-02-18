# Day 4 (Who pays the bills) project
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random

people = len(names)

random_names = random.randint(0,people)
who_pay_the_bills = names[random_names]

print(who_pay_the_bills)