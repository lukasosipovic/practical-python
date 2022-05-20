# bounce.py
#
# Exercise 1.5

height = 100
number_of_times = 0

while number_of_times < 10:
    height *=  0.6
    number_of_times += 1
    print(number_of_times, round(height, 4))