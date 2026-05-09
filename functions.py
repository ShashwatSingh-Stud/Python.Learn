# Parameters and Arguments

# def palindrome(n):
#     rev = 0
#     copy = n
#     while n != 0:
#         rev = rev * 10 + n % 10
#         n = n //10

#     if copy == rev:
#         print("Palindrome.")
#     else:
#         print("not a Palindrome.")

# palindrome(121)
# palindrome(121)
# palindrome(121)
# palindrome(121)
# palindrome(121)
     

# 1. Positional Arguments
# 2. Default Arguments / Keywords Arguments

# def numbers(n):
#     if n == 101:
#         return "done"
#     print(n)
#     numbers(n+1)

# numbers(1)

# n = int(input("Give a Number :- "))

# for i in range(2,(n//2)+1):
    
#     if n % i == 0:
#         print(f"{n} is not a Prime Number. ")
#         break
       
# else:
#         print(f"{n} is a Prime Number. ")   

# n = int(input("Tell me the Number :- "))
# copy = n

# length = len(str(n))

# sum = 0

# while n > 0:
#     digit = n % 10
#     sum += digit**length
#     n = n // 10

# if sum == copy: 
#     print("is the Armstrong Number. ")
# else:
#     print(" is not an Armstrong Number. ")


# s = "shery"
# print(f"Reverse String -> {s[::-1]}")
# print(f"Length of the String is -> {len(s)}")
# print(f"String in Upper Format -> {s.upper()}")
# print(f"String in Lower format -> {s.lower()}")

# s = "ShEry"

# lower = ""
# upper = ""
# for i in s:
#     if i.islower():
#         lower = lower + i
#     elif i.isupper():
#         upper = upper + i

# print(lower + upper)

# str1 = "Phs1!@#$127482dhak"
# alpha = 0
# digit = 0
# special = 0
# for i in str1:
#     if i.isalpha():
#         alpha = alpha + 1
#     elif i.isdigit():
#         digit = digit + 1
#     else:
#         special = special + 1

# print(f"Alphabet Count : {alpha}.")
# print(f"Digit Count : {digit}.")
# print(f"Special Count : {special}.")

# str1 = "Hello"
# str2 = "Hello"
# if len(str1) == len(str2):
#     for i in range(len(str1)):
#         if str1[i] != str2[i]:
#             print("string are not the same")
#             break
#         else:
#             print("Strings are same")

# else:
#     print("both the Strings are of Not the Same length")



# def countvowels():
#     str1 = "Hello"
#     vowels = "AEIOUaeiou"
#     count = 0

#     for i in str1:
#         if i in vowels



# n = input("Provide a String :")

# A = n[::-1]

# print(A)


# s = "Hello"
# rev = ""
# for i in s[::-1]:
#     rev = rev + i
# print(rev)



# n = input("Give a String : ")
# vowels = 0
# consonants = 0
# for i in n:
#     if i in "aieouAEIOU":
#         vowels += 1
#     else:
#         consonants += 1
# print(f"Total Vowels are: {vowels}")
# print(f"Total consonants are: {consonants}")



