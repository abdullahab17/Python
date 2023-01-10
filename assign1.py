print("hello world")
fhand=open('python.txt')
count = 0
for line in fhand:
    count = count+1
print("Line Count: ", count)

imp = fhand.read()
print(len(imp))
