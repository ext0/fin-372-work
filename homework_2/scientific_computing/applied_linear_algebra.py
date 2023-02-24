import numpy as np
import matplotlib.pyplot as plt

## Exercise 1

interest_rate = 0.05

asset_a_duration = 6
asset_b_duration = 4

asset_a_count = 100
asset_b_count = 50

asset_a_period_pay = 1500
asset_b_period_pay = 500

asset_a_returns = np.array([asset_a_period_pay] * asset_a_duration) * asset_a_count
asset_b_returns = np.array([asset_b_period_pay] * asset_b_duration) * asset_b_count

asset_a_npv_adjustment_vector = np.array([(1 / (1 + interest_rate)) ** t for t in range(asset_a_duration)])
asset_b_npv_adjustment_vector = np.array([(1 / (1 + interest_rate)) ** t for t in range(asset_b_duration)])

npv_adjusted_asset_a_return = asset_a_returns.dot(asset_a_npv_adjustment_vector)
npv_adjusted_asset_b_return = asset_b_returns.dot(asset_b_npv_adjustment_vector)

total_return = npv_adjusted_asset_a_return + npv_adjusted_asset_b_return

print("Total NPV of these combined assets is " + str(total_return))
# Total NPV of these combined assets is 892502.7013288848

## Exercise 2

x1 = np.reshape(np.arange(6), (3, 2))
x2 = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
x3 = np.array([[2, 5, 2], [1, 2, 1]])
x4 = np.ones((2, 3))

y1 = np.array([1, 2, 3])
y2 = np.array([0.5, 0.5])

# x1 is [3, 2]
# x2 is [4, 2]
# x3 is [2, 3]
# x4 is [2, 3]
# y1 is [1, 3]
# y2 is [1, 2]

# x1.dot(x2) Invalid
# x2.dot(x1) Invalid
x2.dot(x3) # Valid
# x3.dot(x2) Invalid
x1.dot(x3) # Valid
x4.dot(y1) # Valid
# x4.dot(y2) Invalid
# y1.dot(x4) Invalid
y2.dot(x4) # Valid


## Exercise 3

phi = 0.1
alpha = 0.05

x0 = np.array([900_000, 100_000]) * 1_000_000

A = np.array([[1-alpha, alpha], [phi, 1-phi]])

def simulate(x0, A, T=10):
    """
    Simulate the dynamics of unemployment for T periods starting from x0
    and using values of A for probabilities of moving between employment
    and unemployment
    """
    nX = x0.shape[0]
    out = np.zeros((T, nX))
    out[0, :] = x0

    for t in range(1, T):
        out[t, :] = A.T @ out[t-1, :]

    return out

def plot_simulation(x0, A, T=100):
    X = simulate(x0, A, T)
    fig, ax = plt.subplots()
    ax.plot(X[:, 0])
    ax.plot(X[:, 1])
    ax.set_xlabel("t")
    ax.legend(["Employed", "Unemployed"])
    return ax

plot_simulation(x0, A, 50)

eigvals, eigvecs = np.linalg.eig(A.T)
for i in range(len(eigvals)):
    if eigvals[i] == 1:
        which_eig = i
        break

print(f"We are looking for eigenvalue {which_eig}")

dist = eigvecs[:, which_eig]

# need to divide by sum so it adds to 1
dist /= dist.sum()

print(f"The distribution of workers is given by {dist}")

plt.show()

# The distribution of employed/unemployed workers does not change when the number of workers is 
# multiplied by a factor of 1,000,000. This is as expected, as we're dealing with percentage changes.

