import numpy as np
import pandas as pd

student_info = {
    "name": ["amin", "ali", "reza", "amir", "mohsen", "hossein"],
    "age": np.array([20, 23, np.nan, 22, np.nan, 19]),
    "degree": ["BS", "BS", "MS", "MS", "PHD", "BS"],
    "ins": [True, False, True, False, False, False],
    "gpa": [3.5, 3.7, 3.6, 3.8, 3.9, 4],
}

print(student_info)

student_df = pd.DataFrame(student_info)

print(student_df)
