# l = [12,13,14,15,16]

#special powers
#1 - hetrogeneous nature
# it can store any kind of data types at once 
# l = [12,"hello",12.67,True,print()]

# ordered
# every element in list has a designated position. 

#3 - mutable Nature 
# you can change anything inside the list at any point of Time.

# duplicates
# you can store duplicate elements inside the list. 

#reading a list 
# a = [10,20,30,40,50]

# you will use indexing
# print(a)
# print(a[4],a[-1])

# updating a List 
# a = [10,20,30,40,70]
# a[-1] = 50
# print(a)

#delete : 
# a = [10,20,30,40,50]

# del a[-1]

# print(a)

# creating loops on list

# a = [10,20,30,40,50]

#based on values :
# for i in a:
#     print(i)
# here you will access all the values 10,20,30...


#based on index :

# for i in range(0,len(a)):
#     print(a[i])
# this loop can access your index as well as your values and it gives more control over your list. 

# methods 
# a = [1,2,3,4]
# a.append(5)
# print(a)

# l = []

# for i in range(10,51,10):
#     l.append(i)

# print(l)

# a = [10,20,30,40]

# a.insert(2,35)

# print(a)

# a = [10,20,30]

# a.clear()

# print(a)

# a = [10,20,30,10]

# saved = a.pop(1)

# a.remove(10)

# print(a)

# a = int(input("how many elements you want :- "))

# l = []

# for i in range(a):
#     z = int(input("Tell your Number : "))
#     l.append(z)

# print(l)


# a = eval(input("tell your str"))
# print(a)


# a = [10,20,30,40,50]

# l = []

# for i in range(len(a)-1,-1,-1):
#     l.append(a[i])

# print(l)

# a = [10,20,30,40,50]

# z = len(a)-1

# for i in range(len(a)//2):
#     a[i],a[z] = a[z],a[i]
#     z = z-1

# print(a)

# a = [1,2,-4,-2,1,-5,-2,12,45,8]

# for i in a:
#     if i >= 0:
#         print(i)

# for i in a:
#     if i < 0:
#         print(i)


# l = [1,16,17,23,2,45,89]
# largest_index = 0

# largest = l[0]

# s_largest = l[0]

# s_largest_index = 0

# for i in range(1,len(l)):
#     if l[i] > largest:
#         s_largest = largest
#         largest = i
#         s_largest_index = largest_index

# print(largest)
# print(s_largest)


# l = [1,45,23,48,98,26]

# smallest = l[0]
# s_smallest = l[1]

# for i in l:
#     if i < smallest:
#         s_smallest = smallest
#         smallest = i
#     elif i < s_smallest:
#         s_smallest = i
 

# l = [2,1,3,4,5,6,7]
# for i in range(len(l)-1):
#     if l[i] > l[i+1]:
#         print("List is not sorted")
#         break
# else:
#     print("list is sorted. ")


# Pallindrom :
# l = [2,3,15,15,3,2]

# for i in range(len(l)//2):
#     if l[i] != l[len(l)-1-i]:
#         print("list is not a Pallindrome")
#         break
# else:
#     print("List is Pallindrome. ")

# n = int(input("Size of the List. "))
# l = []
# sum = 0
# for i in range(n):
#     inputs = int(input("tell me the Numbers : "))
#     sum += inputs
#     l.append(inputs)

# print(l)
# print(sum)



# lst = list(map(int, input("Enter elements: ").split()))
# print(lst)
#map(data_types, input)
#split(seperates all the Values and digits)
#list(Converts the value in the form of List Data Structures.)


# d1 = {1:10, 2:20, 3:30}
# d2 = {4:40, 5:50, 6:60}

# for i in d2:
#     d1[i] = d2[i]

# print(d1)
   
# d1 = {1:10, 2:20, 3:30}
# d2 = {3:40, 5:50, 6:60}

# for i in d2:
#     if i in d1.keys():
#         d1[i] = d1[i] + d2[i]
#     else:
#         d1[i] = d2[i]

# print(d1)

# l = [1,1,1,2,2,2,3,3,3,3,3,3,4,4,4,4]

#Rotate a list by k elements
# l = [1,2,3,4,5]
# k = 2

# for i in range (k):
#     last = l[-1]
#     for j in range(len(l)-1,0,-1):
#         l[j] = l[j-1]
#     l[0] = last
# print(l)

#Assign all the 0s at the end of the list 
# l = [0,1,0,3,12]

# j = 0
# for i in range(len(l)):
#     if l[i] != 0:
#         l[i] , l[j] = l[j] , l[i]
#         j = j + 1 
# print(l)


# l = [1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4,4,4,4,6,6,6,6,6,7,7,7]

# d = {}

# for i in l:
#     if i in d.keys():
#         d[i] = d[i] + 1
#     else:
#         d[i] = 1

# print(f"Frequency of the elements are {d}")


# l = [3,2,3,2,2,2]

# d = {}

# for i in l:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1

# for i in d.values():
#     if i % 2 == 0:
#         print("Pair.")
#     else:
#         print("Not Pair.")

# d = {}
 
# for i in nums:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1


# sets

# a = []
# b = {}
# c = set() #Type Conversion 


# s = set() #empty set
# s = {1,1,1,2,2,2,3,3,3,4,4,4,4,5,5,5,5,5,5,6,6,6,6,7}
# print(s)

# Methods in sets

# 1. add()
# 2. update()
# 3. remove()
# 4. discard()
# 5. pop()
# 6. clear()

# 1. add()
s = {1,2,2,3,4,5,6,3,4,5,6}
# s.add(7)

# # 2. update() #For adding Multiple Elements
# s.update([7,8,9])
# print(s)

# # 3.remove()
# s.remove(1)
# print(s)

# 4.discard()
# s.discard(10)
# print(s)

# 5. pop()
# s.pop()  # Removes first element from the set.
# print(s)


#6. clear()





# s1 = {1,2,3,4}
# s2 = {2,3,4,5}
# print(f"Intersection : {s1.intersection(s2)}")
# print(f"Union : {s1.union(s2)}")

# print(f"Difference s1 : {s1.difference(s2)}")
# print(f"Difference s2 : {s2.difference(s1)}")
# print(f"Symmetric Difference : {s1.symmetric_difference(s2)}")


# fs = {10,20,30,40,50}
# fs = frozenset(fs) #frozenset is a function
# # fs.remove(50)
# # print(fs)
# print(fs)




