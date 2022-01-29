str = "away from two three four"
count = 0
for i in str:
    if i == "r":
        found=i
        count = count + 1
position=str.find('y')
print(position)
print("total",found,"found in '",str,"': ", count)
