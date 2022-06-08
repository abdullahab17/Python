# Import cars data
import pandas as pd

cars = pd.read_csv('cars.csv', index_col=0)

# Print out country column as Pandas Series
print(cars["carb"])
print("---------------------------------- \n")

# Print out country column as Pandas DataFrame
print(cars[["carb"]])
print("---------------------------------- \n")

# Print out DataFrame with country and drives_right columns
print(cars[["carb", "gear"]])
print("---------------------------------- \n")

# Print out first 3 observations
print(cars[0:3])
print("---------------------------------- \n")

# Print out observation for Japan
print(cars.loc[["Toyota Corolla"]])  # loc for lable
print("---------------------------------- \n")

# Print out observations for Australia and Egypt
print(cars.iloc[[1, 2]])  # iloc for index number
print("---------------------------------- \n")
# Print out fourth, fifth and sixth observation
print(cars[3:6])
print("---------------------------------- \n")

# Print out drives_right value of Honda Civic
print(cars.loc[["Honda Civic"], "mpg"])
print("---------------------------------- \n")

# Print sub-DataFrame
print(cars.iloc[[4, 5], [1, 2]])
print("---------------------------------- \n")

# Print out drives_right column as Series
print(cars.loc[:, "vs"])
print("---------------------------------- \n")

# Print out drives_right column as DataFrame
print(cars.loc[:, ["mpg"]])
print("---------------------------------- \n")

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[: ,["disp","hp"]])
print("---------------------------------- \n")
