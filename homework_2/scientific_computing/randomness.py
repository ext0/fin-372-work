import numpy as np
import matplotlib.pyplot as plt
import quantecon as qe
import scipy.stats as st

## Exercise 1

random_set = np.random.rand(100000)

random_mean = np.mean(random_set)
random_variance = np.var(random_set)

print(f'Random mean is {random_mean}')
print(f'Random variance is {random_variance}')

# Mean is 0.5, as expected
# Variance is 0.083 (1/12), as expected

## Exercise 2

state_values = ["repaying", "delinquency", "default"]

P = np.array([[0.85, 0.1, 0.05], [0.25, 0.6, 0.15], [0, 0, 1]])

x0 = np.array([1, 0, 0])

mc = qe.markov.MarkovChain(P, state_values)

print(mc.stationary_distributions)

x = x0
for t in range(1000):
    x = mc.P.T @ x

print(x)

# The results check out - given an infinite timeline, the probabilities will ensure that all creditors will default given an infinite timeline.

## Exercise 3

# Come back to this

state_values_employment = [10, 1]

P_employment = np.array([[0.95, 0.05], [0.10, 0.90]])

x0_employment = np.array([0.9, 0.1])

mc_employment = qe.markov.MarkovChain(P_employment, state_values_employment)

fig, ax = plt.subplots(figsize=(10, 8))

# Commented out temporarily

# for iteration in range(30):
#     sim_employment = mc_employment.simulate(50, init=10, num_reps=1_000_000)

#     ax.plot(range(50), np.mean(sim_employment, axis=(0)), alpha=0.4)

# Average long run payment is ~$7 per period per worker

## Exercise 4

asset_a = st.norm(10.0, 5.0)

print(f'Asset A average: {asset_a.mean()}')
print(f'Asset A median: {asset_a.median()}')
print(f'Asset A coefficient of variation: {asset_a.std()/asset_a.mean()}')

asset_b = st.gamma(5.3, scale=2)

print(f'Asset B average: {asset_b.mean()}')
print(f'Asset B median: {asset_b.median()}')
print(f'Asset B coefficient of variation: {asset_b.std()/asset_b.mean()}')

asset_c = st.gamma(5.0, scale=2)

print(f'Asset C average: {asset_c.mean()}')
print(f'Asset C median: {asset_c.median()}')
print(f'Asset C coefficient of variation: {asset_c.std()/asset_c.mean()}')

# I would choose asset B, as the median is high, and the coefficient of variation indicates lower relative risk

