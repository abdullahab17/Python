def greet(lang):
    if lang == "es":
        return "Hola"
    elif lang == "fr":
        return "Bonjour"
    else:
        return "Hello"

print(greet("es"), "Bob")
print(greet("en"))

def add(a,b):
    added = a+b
    return added
print(add(3,5))

def computepay(h, r):
    if h > 40:
        rate = 1.5 *r*(h-40)+(40*r)
        return rate
    else:
        rate1 = h*r

hrs = float(input("Enter Hours:"))
rates = float(input("ENter Rate per hour: "))
print("Pay ",computepay(hrs, rates))
