#a = int(input("Take the 1st Number :-"))
#b = int(input("Take the 2nd Number :-"))
#if a > b:
#    print(a)
#elif b > a:
#    print(b)
#else:
#    print("Both are Equal")

#gen = input("Please Tell Your Gender as char (M or F)")

#if gen == "M" or gen == "m":
 #   print("Good Morning SIR")
#elif gen == "F" or gen == "f":
#    print("Good Morning Maam")
#else:
#    print("Unknown")

#number = int(input("Tell me A number :- "))
#a = number % 2 
#if a == 0:
#    print("It is a Even Number")
#else:
#    print("it is a Odd Number ")

name = input("Please Tell Your Name :")
age = int(input("Please tell Your age :"))

if age >= 18:
    print(f"hlo {name} you are a valid voter")
else: 
    print(f"hlo {name} you are not a valid voter. You can vote after {18-age} years.")
