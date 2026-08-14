import numpy as np

data = np.arange(1, 21)

sample = np.random.choice(data, size=5, replace=False)

print("Population:", data)
print("Sample:", sample)
