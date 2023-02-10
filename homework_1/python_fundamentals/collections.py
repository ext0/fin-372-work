### Python Collections

## Assignment 1
y_1 = ["a", "b", "c"]
z_1 = [1, 2, 3]

y_2 = ["a", "b", "c"]
z_2 = [1, 2, 3]

print(f"Before appending: {y_1}")
y_1.append(z_1)
print(f"After appending: {y_1}")

print(f"Before extending: {y_2}")
y_2.extend(z_1)
print(f"After extending: {y_2}")

## Assignment 2
range_1 = list(range(1, 10))
print(f"Range 1 is {range_1}")

range_2 = list(range(1, 10, 2))
print(f"Range 2 is {range_2}")

## Assignment 3
t = (1, "hello", 3.0)

try:
  t[0] = 100
except:
  print("Correctly failed to modify immutable tuple")

try:
  t.append("!!")
except:
  print("Correctly failed to append to immutable tuple")

try:
  t.sort()
except:
  print("Correctly failed to sort immutable tuple")

try:
  t.reverse()
except:
  print("Correctly failed to reverse immutable tuple")

## Assignment 4
foo = ("good", "luck!")

enumerated_tuple = zip(range(len(foo)), foo)

print(f"Output of enumerate(...): {list(enumerate(foo))}")
print(f"Output of custom logic: {list(enumerated_tuple)}")

# Assignment 5
ticker_values = {
  "AAPL": 175.96,
  "GOOGL": 1047.43,
  "TVIX": 8.38
}

# Assignment 6
australia_data = {
  "year": 2018,

  "land_usage": {
    "agricultural": 46.65,
    "forest": 13.42,
    "other": 33.42
  },

  "major_rivers": ["Murray", "Darling", "Murrumbidgee", "Lachlan", "Cooper", "Flinders"]
}

# Assignment 7
australia_data.pop("year")

# Assignment 8
print(australia_data)

# Assignment 9
repeated_set_example = {1, 2, 1, 2, 1, 2}
print(repeated_set_example)

# Assignment 10
s2 = {"hello", "world"}
print("s2 has type", type(s2))
print("s2 has len", len(s2))