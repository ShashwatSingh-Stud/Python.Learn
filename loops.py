#for i in range(50,151,1):
#    print(i)
#for a in range(20,31):
#    print(a)
#for b in range(-12,11):
#    print(b)

#for c in range(10,-11,-1):
#    print(c)

#for i in range (5,51,5):
#    print(i)

#a = int(input())

#for i in range(a,a*10+1,a):
# print(i)

#for i in range(100):
#    print("Hello World")

#n = int(input("Provide a Number"))
#for i in range(1,n+1):
# print(i)

# for i in range(1,6,1):
#     print(i)

# for i in range(1,11,1):
#     print(i)

# for i in range(10,0,-1):
#     print(i)


# n = int(input("Pls tell number :- "))

# for i in range(n,0,-1):
#     print(i)

# a = int(input("Pls tell a Number :- "))
# for i in range(1,11,1):
#     print(f"{a} x {i} = {a*i}")


# n = int(input("Tell a Number :- "))
# a = 0

# for i in range(1,n+1):
#     a = a + i

#     print(a)

# n = int(input("Tell a Number :- "))
# a = 0

# for i in range(2,n+1,2):
#     a = a + i

#     print(a)

# n = int(input("give me a Number :- "))
# esum = 0
# osum = 0
# for i in range(1,n+1):
#     if i % 2 == 0:
#         esum = esum + i
#     else:
#         osum = osum + i
        
# print(f"even sum is {esum} and odd sum is {osum}.")


# n = int(input("Give a Number :- "))

# for i in range(1,n+1):
#     if n % i == 0:
#         print(f"{i} is the factor of the Number {n}. ")

# a = int(input("Provide a Number :- "))
# copy=a
# # sum = 0
# # for i in range(1,a):
# #     if a % i == 0:
# #         sum = sum + i

# if sum == copy:
#         print("your number is perfect.")
# else:
#         print("Not a perfect number.")


# n = int(input("Pls Provide a Number :- "))
# count = 0
# for i in range(1,n+1):
#     if n % i == 0:
#         count = count + 1

# if count == 2:
#     print("My Number is Prime.")
# else:
#     print("My Number is Composite.")

 
# n = int(input("Pls Provide a Number :- "))

# for i in range(2,(n//2)+1):
#     if n % i == 0:
#          print("its a Composite Number.")
#          break

# else:
#     print("Its A Prime Number.")

# a = 0
# b = 1 
# n = int(input("Enter Your Series Number :- "))

# for i in range(n):
#     print(a)
#     a , b = b , a+b

# n = int(input("Enter a Number: "))
# lar = 0

# for i in str(n):
#     a = int(i)
#     if a > lar:
#         lar = a
#         print(lar)

# Guessing Game

# import random

# akshay = random.randint(1,10)

# for i in range(5):
#     tanishq = int(input("Enter Your Number :- "))

#     if tanishq == akshay:
#         print("You won.")
#         break

#     if tanishq > akshay:
#         print("Your Guess is too High")

#     if tanishq < akshay:
#         print("Your Guess Is Too Low.")

# else:
#     print(f"Bhaiya Haar Gye.Number h {akshay}.")        

# Pallindrom Checking

# num = 1221
# if str(num) == str(num)[::-1]:
#     print("Your Number Is Pallindrom.")
# else:
#     print("Not a pallindrom. ")

 
# sum = 0 
# while True:
#     n = int(input("Enter Your Number:- "))

#     if n == 0:
#         break
#     sum += n
# print(sum)


# Armstrong Number :
 
n = int(input("Enter a Number :- "))
copy = n

length = len(str(n))
sum = 0
while n > 0:
    digit = n % 10
    sum += digit**length
    n = n // 10

if copy == sum:
    print("Armstrong Number")
else:
    print("Not An Armstrong Number")







