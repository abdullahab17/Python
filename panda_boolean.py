import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
print(cars)
# Extract drives_right column as Series: dr
dr = cars["gear"] < 4
print(dr)

# Use dr to subset cars: sel
sel = cars[dr]
print(sel)
# Convert code to a one-liner
sal = (cars[cars['cyl'] == 6])
print(sal)

