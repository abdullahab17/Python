class Player:
    MAX_POSITION = 10
    MAX_SPEED = 5
    def __init__(self):
        self.position = 0

    # Add a move() method with steps parameter
    def move(self, steps):
        if self.position + steps < Player.MAX_POSITION:
            self.position = self.position + steps
        else:
            self.position = Player.MAX_POSITION

    # This method provides a rudimentary visualization in the console
    def draw(self):
        drawing = "-" * self.position + "|" + "-" * (Player.MAX_POSITION - self.position)
        print(drawing)


p = Player();
p.draw()
p.move(4);
p.draw()
p.move(5);
p.draw()
p.move(3);
p.draw()

# Create Players p1 and p2
p1, p2 = Player(), Player()

print("MAX_SPEED of p1 and p2 before assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

# Assign 7 to p1.MAX_SPEED
Player.MAX_SPEED = 7

print("MAX_SPEED of p1 and p2 after assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

print("MAX_SPEED of Player:")
# Print Player.MAX_SPEED
print(Player.MAX_SPEED)
print("---------------------------------------------------------------------------------------------------\n")

class BetterDate:
    # Constructor
    def __init__(self, year, month, day):
        # Recall that Python allows multiple variable assignments in one line
        self.year, self.month, self.day = year, month, day

    # Define a class method from_str
    @classmethod
    def from_str(cls, datestr):
        # Split the string at "-" and convert each part to integer
        parts = datestr.split("-")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        # Return the class instance
        return cls(year, month, day)


bd = BetterDate.from_str('2020-04-30')
print(bd.year)
print(bd.month)
print(bd.day)
print("---------------------------------------------------------------------------------------------------\n")

# import datetime from datetime
from datetime import datetime


class BetterDate:
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day

    @classmethod
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)

    # Define a class method from_datetime accepting a datetime object
    @classmethod
    def from_datetime(cls, dateobj):
        year, month, day = dateobj.year, dateobj.month, dateobj.day
        return cls(year, month, day)

    # You should be able to run the code below with no errors:


today = datetime.today()
bd = BetterDate.from_datetime(today)
print(bd.year)
print(bd.month)
print(bd.day)
print("---------------------------------------------------------------------------------------------------\n")


class Employee:
    def __init__(self, name, salary=30000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount


class Manager(Employee):
    def display(self):
        print("Manager ", self.name)

    def __init__(self, name, salary=50000, project=None):
        Employee.__init__(self, name, salary)
        self.project = project

    # Add a give_raise method
    def give_raise(self, amount, bonus=1.05):
        new_amount = amount * bonus
        Employee.give_raise(self, new_amount)


mngr = Manager("Ashta Dunbar", 78500)
mngr.give_raise(1000)
print(mngr.salary)
mngr.give_raise(2000, bonus=1.03)
print(mngr.salary)