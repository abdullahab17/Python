import matplotlib.pyplot as plt
import pandas as pd
avocados =pd.read_pickle("avoplotto.pkl")
print(avocados.head())

# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby("size")["nb_sold"].sum()

# Create a bar plot of the number of avocados sold by size
nb_sold_by_size_bar= nb_sold_by_size.plot(kind="bar")
# Show the plot
plt.show()
print("---------------------------------\n")

# Get the total number of avocados sold on each date
nb_sold_by_date = avocados.groupby("date")["nb_sold"].sum()

# Create a line plot of the number of avocados sold by date
nb_sold_by_date_line = nb_sold_by_date.plot(kind="line")

# Show the plot
plt.show()
print("---------------------------------\n")

# Scatter plot of avg_price vs. nb_sold with title
avocados.plot(x="nb_sold",y="avg_price",title="Number of avocados sold vs. average price",kind="scatter")

# Show the plot
plt.show()
print("---------------------------------\n")
# Histogram of conventional avg_price
avocados[avocados["type"]=="conventional"]["avg_price"].hist(alpha=0.5,bins=20)

# Histogram of organic avg_price
avocados[avocados["type"]=="organic"]["avg_price"].hist(alpha=0.5,bins=20)

# Add a legend
plt.legend(["conventional","organic"])

# Show the plot
plt.show()
print("---------------------------------\n")

# Create a list of dictionaries with new data
avocados_list = [
    {"date":"2019-11-03", "small_sold":10376832,"large_sold": 7835071},
    {"date": "2019-11-10", "small_sold": 10717154,"large_sold": 8561348},
]

# Convert list into DataFrame
avocados_2019 = pd.DataFrame(avocados_list)

# Print the new DataFrame
print(avocados_2019)
print("---------------------------------\n")

# Create a dictionary of lists with new data
avocados_dict = {
  "date": ["2019-11-17","2019-12-01"],
  "small_sold": [10859987,9291631],
  "large_sold": [7674135,6238096]
}

# Convert dictionary into DataFrame
avocados_2019_d = pd.DataFrame(avocados_dict)

# Print the new DataFrame
print(avocados_2019_d)

print("---------------------------------\n")
# Read CSV as DataFrame called airline_bumping
airline_bumping = pd.read_csv("airline_bumping.csv")

# Take a look at the DataFrame
print(airline_bumping)