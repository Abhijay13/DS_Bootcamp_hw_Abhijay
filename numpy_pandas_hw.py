# HW Questions (NumPy and Pandas)

import numpy as np
import pandas as pd

# -----------------------------
# NumPy Section
# -----------------------------

# Define two custom numpy arrays, A and B
A = np.array([2, 5, 8, 10, 12])
B = np.array([5, 10, 15, 20, 25])

# Stack A and B vertically and horizontally
v_stack = np.vstack((A, B))
h_stack = np.hstack((A, B))

print("Vertical Stack:\n", v_stack)
print("\nHorizontal Stack:\n", h_stack)

# Find common elements between A and B
common_elements = np.intersect1d(A, B)
print("\nCommon elements between A and B:", common_elements)

# Extract numbers from A between 5 and 10 (inclusive)
range_elements = A[(A >= 5) & (A <= 10)]
print("\nElements in A between 5 and 10:", range_elements)

# Filter rows of iris_2d where petallength > 1.5 and sepallength < 5.0
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

filtered_rows = iris_2d[(iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0)]
print("\nFiltered iris_2d rows (petallength > 1.5 and sepallength < 5.0):\n", filtered_rows)

# -----------------------------
# Pandas Section
# -----------------------------

# Filter 'Manufacturer', 'Model', and 'Type' for every 20th row starting from 0
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
filtered_df = df.loc[::20, ['Manufacturer', 'Model', 'Type']]
print("\nEvery 20th row (Manufacturer, Model, Type):\n", filtered_df)

# Replace missing values in Min.Price and Max.Price columns with their mean
df['Min.Price'].fillna(df['Min.Price'].mean(), inplace=True)
df['Max.Price'].fillna(df['Max.Price'].mean(), inplace=True)
print("\nMissing values replaced with mean in Min.Price and Max.Price:\n", df[['Min.Price', 'Max.Price']].head())

# Get rows of a DataFrame with row sum > 100
df2 = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4), columns=['A', 'B', 'C', 'D'])
rows_gt_100 = df2[df2.sum(axis=1) > 100]
print("\nRows where sum > 100:\n", rows_gt_100)
