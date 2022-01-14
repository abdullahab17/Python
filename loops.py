n = 1
while n > 0:
    print(n)
    n=n-1
print("BLAST")
print(n)

for i in [5,4,3,2,1]:
    print(i)
print("Done.")

for i in ["Max","Giovani","Juan"]:
    print("Hello !",i)
print("Done")

largest_so_far = -1
print("Before ", largest_so_far)
for i in [9,41,12,3,74,15]:
    if i > largest_so_far:
        largest_so_far = i
    print(largest_so_far, i)
print("After !",largest_so_far)


count = 0
print("Before: ",count)
for i in [9,41,12,3,74,15]:
    count = count +i
    print(count,"|",i)
print("After: ",count)

found = False
print("Before: ",found)
for i in [9,41,12,3,74,15]:
    if i ==3:
        found = True
        break
    print(found,i)
print("After: ",found)


smallest_so_far = None
print("Before ", largest_so_far)
for i in [9,41,12,3,74,15]:
    if smallest_so_far is None:
        smallest_so_far = i
    elif i < smallest_so_far:
        smallest_so_far = i
    print(smallest_so_far, i)
print("After !",smallest_so_far)

tot = 0
for i in [5,4,3,2,1]:
    tot = tot +1
print(tot)

#n = 0
#t = 0.0
#while True:
#    sval = input("Enter number: ")
#    if sval == "done":
#        break
#    try:
#        fval = float(sval)
#    except:
#        print("Invalid Input")
#        continue
#    n = n+1
#    t = t+fval
#print("Total:",tot,"\nNumbers: ",n,"\nAverage: ",t/n)


largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num= int(num)
        if largest is None or largest < num:
            largest = num
        elif smallest is None or  smallest > num:
            smallest = num
    except:
        print("Invalid input")
        continue

print("Maximum is", largest)
print("Minimum is",smallest)
