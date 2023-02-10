### Python Collections

## Assignment 1
zero_coupon_bond_value = 100 / (1 + 0.05)**10
print(f"Zero coupon bond value is {zero_coupon_bond_value}")

## Assignment 2

# Control flow 1
x = 1

if x > 0:
  print("1")
  print("2")
print("3")

# Control flow 2
x = 1

if x > 0:
  print("1")
print("2") # changed the indentation
print("3")

## Assignment 3
import datetime
current_time = datetime.datetime.now()
if (current_time.hour > 12):
  print("Good afternoon!")

## Assignment 4
import numpy as np
x = np.random.random()
print(f"x = {x}")

## Assignment 5

# Discount rate
r = 0.05

# High school wage
w_hs = 40_000

# College wage and cost of college
c_college = 5_000
w_college = 50_000

highschool_wage_pv_array = []
college_tuition_pv_array = []
college_wage_pv_array = []

# Compute npv of being a hs worker
for n in range(0, 40):
  present_value_of_wage = w_hs / ((1 + r)**n)
  highschool_wage_pv_array.append(present_value_of_wage)

# Compute npv of attending college
for n in range(0, 4):
  present_value_of_tuition = -c_college / ((1 + r)**n)
  college_tuition_pv_array.append(present_value_of_tuition)

# Compute npv of being a college worker
for n in range(4, 40):
  present_value_of_wage = w_college / ((1 + r)**n)
  college_wage_pv_array.append(present_value_of_wage)

# Is npv_collegeworker - npv_collegecost > npv_hsworker
npv_college_wage = sum(college_wage_pv_array)
npv_college_tuition = sum(college_tuition_pv_array)

npv_highschool_wage = sum(highschool_wage_pv_array)

print(f"College tuition PV is {npv_college_tuition}")
print(f"College wage PV is {npv_college_wage}")
print(f"Total college PV is {npv_college_wage - npv_college_tuition}")
print(f"")
print(f"High school wage PV is {npv_highschool_wage}")

## Assignment 6
cities = ["Phoenix", "Austin", "San Diego", "New York"]
states = ["Arizona", "Texas", "California", "New York"]

for city, state in zip(cities, states):
  print(f"{city} is in {state}")

## Assignment 7

# Define cost of teaching python
cost = 25_000
r = 0.01

# Per month value
added_value = 2500

n_months = 0
total_npv = 0.0

# Put condition below here
while (total_npv < cost): # (replace False with your condition here)
    n_months = n_months + 1  # Increment how many months they've worked

    total_npv = total_npv + (added_value / (1 + r) ** n_months)

print(f"It will take {n_months} months for the internal investment to pay off")

## Assignment 8

x = np.random.rand(10_000)
threshold = 0.999

found_index = None

for index in range(len(x)):
  value = x[index]
  if value > threshold:
    found_index = index
    break

print(f"Found a value above {threshold} at {found_index}")

## Assignment 9
x = np.random.rand(10_000)
threshold = 0.5
sum = 0

for index in range(len(x)):
  value = x[index]
  if value < threshold:
    continue
  sum = sum + value

print(f"Sum of random values was {sum}")

## Assignment 10
cities = ["Phoenix", "Austin", "San Diego", "New York"]
states = ["Arizona", "Texas", "California", "New York"]

output_strings = [f"{city} is in {state}" for city, state in zip(cities, states)]
print(output_strings)

