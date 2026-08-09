import numpy as np

marks = np.array([45, 78, 32, 90, 55])

result = np.where(marks >= 50, "Pass", "Fail")

print(result)