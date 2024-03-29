def square(value):
    new_value = value ** 2
    return new_value


num = square(6)
print(num)
print("-------------------------------------------------------")


# Define the function shout
def shout():
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = "congratulations" + "!!!"

    # Print shout_word
    print(shout_word)


# Call shout
shout()
print("-------------------------------------------------------")


# Define the function shout
def shout():
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = "congratulations" + "!!!"

    # Print shout_word
    print(shout_word)


# Call shout
shout()
print("-------------------------------------------------------")


# Define shout with the parameter, word
def shout(word):
    """Return a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + "!!!"

    # Replace print with return
    return shout_word


# Pass 'congratulations' to shout: yell
yell = shout("congratulations")

# Print yell
print(yell)
print("-------------------------------------------------------")


def raise_to_power(val1, val2):
    new_val1 = val1 ** val2
    new_val2 = val2 ** val1
    new_val = (new_val1, new_val2)
    return new_val


res = raise_to_power(2, 3)
print(res)
print("-------------------------------------------------------")


# Define shout with parameters word1 and word2
def shout(word1, word2):
    """Concatenate strings with three exclamation marks"""
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + "!!!"

    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + "!!!"

    # Concatenate shout1 with shout2: new_shout
    new_shout = shout1 + shout2

    # Return new_shout
    return new_shout


# Pass 'congratulations' and 'you' to shout(): yell
yell = shout("congratulations", "you")

# Print yell
print(yell)
print("-------------------------------------------------------")


# Define shout_all with parameters word1 and word2
def shout_all(word1, word2):
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + "!!!"

    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + "!!!"

    # Construct a tuple with shout1 and shout2: shout_words
    shout_words = (shout1, shout2)

    # Return shout_words
    return shout_words


# Pass 'congratulations' and 'you' to shout_all(): yell1, yell2
yell1, yell2 = shout_all('congratulations', 'you')

# Print yell1 and yell2
print(yell1)
print(yell2)
print("-------------------------------------------------------")

# Import pandas
import pandas as pd

# Import Twitter data as DataFrame: df
df = pd.read_csv("tweets.csv")

# Initialize an empty dictionary: langs_count
langs_count = {}

# Extract column from DataFrame: col
col = df['lang']

# Iterate over lang column in DataFrame
for entry in col:

    # If the language is in langs_count, add 1
    if entry in langs_count.keys():
        langs_count[entry] += 1
    # Else add the language to langs_count, set the value to 1
    else:
        langs_count[entry] = 1

# Print the populated dictionary
print(langs_count)
print("-------------------------------------------------------")


# Define count_entries()
def count_entries(df, col_name):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: langs_count
    langs_count = {}

    # Extract column from DataFrame: col
    col = df[col_name]

    # Iterate over lang column in DataFrame
    for entry in col:

        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            langs_count[entry] += 1
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry] = 1

    # Return the langs_count dictionary
    return langs_count


# Call count_entries(): result
result = count_entries(tweets_df, 'lang')

# Print the result
print(result)