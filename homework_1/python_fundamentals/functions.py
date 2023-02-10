### Python Collections

## Assignment 1
def cobb_douglas(K, L):
  # Create alpha and z
  z = 1
  alpha = 0.33

  return z * K**alpha * L**(1 - alpha)

print(cobb_douglas(0.5, 0.75))

## Assignment 2

def variance(L):
  average = sum(L) / len(L)
  return sum([(x - average)**2 for x in L]) / (len(L) - 1)

print(variance([1, 10, 10, 10, 10]))

## Assignment 3
def returns_to_scale(K, L, gamma):
  """  
  Utilizes the Cobb Douglas algorithm to determine the returns to scale when K and L are scaled by gamma, and returns the ratio of returns
  """
  y1 = cobb_douglas(K, L)
  y2 = cobb_douglas(gamma*K, gamma*L)
  y_ratio = y2 / y1
  return y_ratio / gamma

## Assignment 4
print("Foo", "Bar", sep="_", end="!")