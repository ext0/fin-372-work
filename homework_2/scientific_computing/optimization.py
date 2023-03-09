import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize_scalar

## Exercise 1

B = 1.5
A = np.linspace(0, 10, 100)

def U(A, B, alpha=1/3):
  return B**alpha * A**(1-alpha)

def A_bc(B, W=20, pa=2, pb=1):
  "Given B, W, and pa return the max amount of A our consumer can afford"
  return (W - (B * pb)) / pa

def B_ac(A, W=20, pa=2, pb=1):
  "Given A, W, and pb return the max amount of B our consumer can afford"
  return (W - (A * pa)) / pb

def objective(B, W=20, pa=2):
  """
  Return value of -U for a given B, when we consume as much A as possible

  Note that we return -U because scipy wants to minimize functions,
  and the value of B that minimizes -U will maximize U
  """
  A = A_bc(B, W, pa)
  return -U(A, B)

def show_contour_utility_function():
  fig, ax = plt.subplots()
  B = np.linspace(0, 20, 100).reshape((100, 1))
  contours_utility = ax.contourf(A, B.flatten(), U(A, B), levels=20)

  fig.colorbar(contours_utility)

  ax.plot(A, np.vectorize(B_ac)(A))
  ax.set_xlabel("A")
  ax.set_ylabel("B")
  ax.set_title("U(A,B)")

  plt.show()

def minimize_function():
  result = minimize_scalar(objective)
  optimal_B = result.x
  optimal_A = A_bc(optimal_B, 20, 2)
  optimal_U = U(optimal_A, optimal_B)

  print("The optimal U is ", optimal_U)
  print("and was found at (A,B) =", (optimal_A, optimal_B))

# show_contour_utility_function()

## Exercise 2

C = 1.5
P = np.linspace(0, 10, 100)

def U_2(P, C):
  return (-(P - 20) ** 2) - 2 * ((C - 1) ** 2)

def P_C(C, W=100, pc=2, pp=1):
  "Given C, W, and pc return the max amount of P our consumer can afford"
  return (W - (C * pc)) / pp

def C_P(P, W=10, pc=2, pp=1):
  "Given P, W, and pp return the max amount of C our consumer can afford"
  return (W - (P * pp)) / pc

def objective(C, W=10, pc=2, pp=1):
  """
  Return value of -U for a given B, when we consume as much A as possible

  Note that we return -U because scipy wants to minimize functions,
  and the value of B that minimizes -U will maximize U
  """
  P = P_C(C, W, pc, pp)
  return -U_2(P, C)

def show_contour_utility_function():
  fig, ax = plt.subplots()
  C = np.linspace(0, 20, 100).reshape((100, 1))
  contours_utility = ax.contourf(P, C.flatten(), U_2(P, C), levels=20)

  fig.colorbar(contours_utility)

  ax.plot(P, np.vectorize(C_P)(P))
  ax.set_xlabel("P")
  ax.set_ylabel("C")
  ax.set_title("U(P,C)")

  plt.show()

def minimize_function(W, pc, pp):
  result = minimize_scalar(objective, args=(W, pc, pp))
  optimal_C = result.x
  optimal_P = P_C(optimal_C, W, pc, pp)
  optimal_U = U_2(optimal_P, optimal_C)

  print("The optimal U is ", optimal_U)
  print("and was found at (P,C) =", (optimal_P, optimal_C))

# W = 10, p_P = 1, and p_C = 2
minimize_function(10, 1, 2)

# W = 50, p_P = 1, and p_C = 2
minimize_function(50, 1, 2)

# W = 150, p_P = 1, and p_C = 2
minimize_function(150, 1, 2)