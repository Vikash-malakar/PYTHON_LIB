import numpy as np

marks = np.array([
    [80, 75, 90],
    [65, 70, 72],
    [90, 95, 88],
    [55, 60, 58]
])

print("Total marks:", np.sum(marks, axis=1))
print("Average:", np.mean(marks, axis=1))
print("Highest:", np.max(marks, axis=1))
print("Lowest:", np.min(marks, axis=1))

print("Subject average:", np.mean(marks, axis=0))