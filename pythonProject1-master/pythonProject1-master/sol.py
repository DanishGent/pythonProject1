"""files"""
mydata = ["this is,\n", "kalto he is.\n", "43 in age.\n"]
myfile = "../data/input01.txt"


with open(myfile, "w") as file:
    file.writelines(mydata)

line_number = 0
with open(myfile) as file:
    for line in file:
        line_number += 1
        print(line.strip())
    print()



""" inventory """
      split epul then put bigest to middle

""" turtle hunt """
        remove hier weiter

""" cars """
def drive_car():
    print("guy1: hey pal you ok?  guy2: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!!!")


car1_wheels = 6
car1_maxspeed = 360
car2_wheels = 3
car2_maxspeed = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

print("wheels", car1_wheels, "maximum speed", car1_maxspeed)
print("wheels", car2_wheels, "maximum speed", car2_maxspeed)

drive_car()


""" morris """

def sleep():
    status["sleepiness"] -= 10

def mine():
    status["sleepiness"] += 5
    status["thirst"] += 5
    status["hunger"] += 5
    status["whisky"] += 0
    status["gold"] += 5

def drink():
    status["sleepiness"] += 5
    status["thirst"] -= 6
    status["hunger"] -= 6
    status["whisky"] += 0
    status["gold"] -= 2

def dead():
    return status["sleepiness"] > 100 or status["thirst"] > 100 or status["hunger"] > 100


status = {"turn": 0, "sleepiness": 0, "thirst": 0, "hunger": 0, "whisky": 0, "gold": 0}  # dictionary

while not dead() and status["turn"] < 1000:
    status["turn"] += 1
    sleep()
    mine()
    drink()
    sleep()
    print(status)

"""  double_this """
def double_this(x):
    return x * 2

print(double_this(3))

""" factorial """
def factorial(x):


    if x == 1:
        return 1
    else:

        return (x * factorial(x-1))

num = 6

result = factorial(num)
print( num, "! =", result)

""" print_pattern """
def print_repeatedly(string, repetitions):
    str = ""
    for x in range(repetitions):
        str = str + string
    print(str)

print_repeatedly("xy", 6)


def print_pattern(string, repetition_list):
    for x in repetition_list:
        print_repeatedly(string, x)


print_pattern("abc", [4, 2, 1])

""" turtle """
import turtle


def visible(turtle_name):

    return 0


def demo():
    tom = turtle.Turtle()
    print(type(tom))
    tom.speed(1)
    for x in range(5):
        tom.forward(50)
        tom.left(90)
        print(f'Tom is now at {tom.position()}, x-value: {tom.position()[0]=:.2f}, y-value: {tom.position()[1]=:.2f}')
    tom.penup()
    tom.forward(100)
    tom.pendown()
    tom.pencolor("red")
    tom.right(90)
    tom.forward(120)
    tom.right(-90)
    tom.forward(120)
    tom.home()
    turtle.done()


demo()
