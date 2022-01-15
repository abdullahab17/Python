first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

#adding both lists
full = first + second

#sorting the new list
full_sorted = sorted(full)

#sorting in desc order
full_sort = sorted(full,reverse = True)
print(full_sorted)
print(full_sort)
#--------------------------------------------------------------------------

place = "poolhouse"

# Use upper() on place: place_up
#place_up = upper(place)
print(place.upper())
# Print out place and place_up
print(place)


# Print out the number of o's in place
print(place.count("o"))
#--------------------------------------------------------------------------

areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))
#-------------------------------------------------------------------------
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)


# Print out areas
print(areas)

#reverse order of elementes in areas
areas.reverse()
print(areas)
