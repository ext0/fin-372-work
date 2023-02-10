### Python Fundamentals

## Assignment 1
z = 3
z = z + 4
print(f"z is {z}")

## Assignment 2
x = "Hello World"
print(f"Length of '{x}' is {len(x)}")

## Assignment 3 & 4
import time as t

t.localtime()

# Assignment 5
D = 10000.0
r = 0.025
T = 30

## Assignment 6
PDV = D / ((1 + r) ** T)
print(f"PDV is {PDV}")

## Assignment 7
import math

x = 1.05
y = 1.02

log_difference = math.log(x) - math.log(y)
print(f"Log difference is {log_difference}")

## Assignment 8
x = 'What\'s wrong with this string'

## Assignment 9
x = "Hello"
y = "World"
print(x, y)

## Assignment 10
test = "abc"
new_test = test.replace("c", "d")
print(f"{test} -> {new_test}")

## Assignment 11
price = "$6.50"
clean_price = price.replace("$", "")
parsed_price = float(clean_price)
print(f"Price is {parsed_price}")

## Assignment 12 / 13
country = "Brazil"
GDP = 1610
year = 2021
my_string = f"{country} had ${GDP} billion GDP in {year}"
print(my_string)

## Assignment 14
first_quarter_label = "1st"
first_quarter_revenue = 110

second_quarter_label = "2nd"
second_quarter_revenue = 95

third_quarter_label = "3rd"
third_quarter_revenue = 100

fourth_quarter_label = "4th"
fourth_quarter_revenue = 130

print(f"The {first_quarter_label} quarter revenue was {first_quarter_revenue}M")
print(f"The {second_quarter_label} quarter revenue was {second_quarter_revenue}M")
print(f"The {third_quarter_label} quarter revenue was {third_quarter_revenue}M")
print(f"The {fourth_quarter_label} quarter revenue was {fourth_quarter_revenue}M")

## Assignment 15
x = 2
y = 2
z = 4

# Statement 1
x > z # -> False

# Statement 2
x == y # -> True

# Statement 3
(x < y) and (x > y) # -> False

# Statement 4
(x < y) or (x > y) # -> False

# Statement 5
(x <= y) and (x >= y) # -> True

# Statement 6
True and ((x < z) or (x < y)) # -> False

## Assignment 16

all([True, True, True]) # -> True
all([False, True, False]) # -> False
all([False, False, False]) # -> False
any([True, True, True]) # -> True
any([False, True, False]) # -> True
any([False, False, False]) # -> False
