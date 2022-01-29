#Abdullah (18B-015-CS)
#Lab 5
#Excercise 1 2 3 4
class Boy:
    name =""
    gender ="Male"
    age = 20
class Girl:
    name =""
    gender ="Female"
    age = 18

Irtiza = Boy()
Ahmed = Boy()
Arisha = Girl()
Ayesha = Girl()
print("My name is : " + "Irtiza")
Irtiza.gender
print(Irtiza.gender)
Irtiza.age = 21
print(Irtiza.age)
print("My name is : " + "Ahmed")
Ahmed.gender
print(Ahmed.gender)
Ahmed.age = 22
print(Ahmed.age)
print("My name is : " + "Arisha")
Arisha.gender
print(Arisha.gender)
Arisha.age = 19
print(Arisha.age)
print("My name is : " + "Ayesha")
Ayesha.gender
print(Ayesha.gender)
Ayesha.age =18
print(Ayesha.age)


#Excercise 5 6
class Fish:
    def __init__(self, first_name, last_name="Fish", skeleton="bone", eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids
    def swim(self):
        print("The fish is swimming.")
    def swim_backwards(self):
        print("The fish can swim backwards.")

class Trout(Fish):
    pass

terry = Trout("Terry")
print(terry.first_name + " " + terry.last_name)
print(terry.skeleton)
print(terry.eyelids)
terry.swim()
terry.swim_backwards()

#Excercise 7
class Shark(Fish):
    def __init__(self, first_name, last_name="Shark",
        skeleton="cartilage", eyelids=True):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids
    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")

sammy = Shark("Sammy")
print(sammy.first_name + " " + sammy.last_name)
sammy.swim()
sammy.swim_backwards()
print(sammy.eyelids)
print(sammy.skeleton)

#Excercise 8
class Trout(Fish):
    def __init__(self, water = "freshwater"):
        self.water = water
        super().__init__(self)
terry = Trout()
terry.first_name = "Terry"
print(terry.first_name + " " + terry.last_name)
print(terry.eyelids)
print(terry.water)
terry.swim()

class Coral:
    def community(self):
        print("Coral lives in a community.")
class Anemone:
    def protect_clownfish(self):
        print("The anemone is protecting the clownfish.")
class CoralReef(Coral, Anemone):
    pass

great_barrier = CoralReef()
great_barrier.community()
great_barrier.protect_clownfish()

#Task 2
class Emirates:
    def __init__(self, flight_no, flight_name, arrival_date,arrival_city,  Departure_date, Departure_city):
        self.flight_no = flight_no
        self.flight_name = flight_name
        self.arrival_date = arrival_date
        self.arrival_city = arrival_city
        self.Departure_date = Departure_date
        self.Departure_city = Departure_city

    def flight_details(self):
        return "Flight No: {} \nFlight Name: {}\nArrival Date: {}\nArrival City: {}\nDeparture Date: {}\nDeparture City: {}".format(self.flight_no,self.flight_name,self.arrival_date,self.arrival_city,self.Departure_date,self.Departure_city)

class Passenger(Emirates):
    def __init__(self, flight_no, flight_name, arrival_date,arrival_city,  Departure_date, Departure_city,age_of_passenger):
        super().__init__(flight_no,flight_name,arrival_date,arrival_city,Departure_date,age_of_passenger)
        self.age_of_passenger = age_of_passenger
a = Emirates("AK123","Emirates","10 Oct","Karachi","9 Oct","Dubai")
b = Passenger("AK123","Emirates","10 Oct","Karachi","9 Oct","Dubai",29)
print(a.flight_details())
print(b.age_of_passenger)

#Task 3
class Umbrella:
    def __init__(self,style,prints,sizes):
        self.style = style
        self.prints = prints
        self.sizes = sizes
    def details(self):
        return "--> This Umbrella has {} style and has {} prints on it with a size of {}\n".format(self.style,self.prints,self.sizes)
class Canopy(Umbrella):
    def __init__(self,style,prints,sun_protection):
        super().__init__(style,prints,sun_protection)
        self.sun_protection = sun_protection
class Classic(Umbrella):
    def __init__(self,style,prints,for_adults):
        super().__init__(style,prints,for_adults)
        self.for_adults = for_adults

u = Umbrella("Modern","Zebra","Medium")
can = Canopy("Modern","Zebra","Used for sun protection")
cl = Classic("Old Fashioned","No","is msinly used by adults")
print(u.details())
#print(can.sun_protection)
print(can.details())
print(cl.details())
#print(cl.for_adults)
