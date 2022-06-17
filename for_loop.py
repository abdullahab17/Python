import numpy as np

np_height = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
np_baseball = np.array([10, 11, 12, 13, 14, 15])
# For loop over np_height
for i in np.nditer(np_height):
    print(i)

# For loop over np_baseball
for i in np.nditer(np_baseball):
    print(i)
print("==================================================\n")
import pandas as pd

# Import cars data
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows():
    #print(lab)
    #print(row)
    print(lab + ":" + str(row['gear']))
    #cars.loc[lab, "COUNTRY"] = row["country"].upper()

print("==================================================\n")

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, a in enumerate(areas):
    index = index + 1
    # print(str(index),": ",str(a))
    print("{}: {}".format(index, a))
print("==================================================\n")

# house list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Build a for loop from scratch
for i in house:
    print("the {} is {} sqm".format(i[0], i[1]))
print("==================================================\n")

# Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin',
          'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw', 'austria': 'vienna'}

# Iterate over europe
for k, v in europe.items():
    print("the capital of", k, "is", v)
print("==================================================\n")




print("==================================================\n")
