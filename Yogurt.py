#comparision Operator
# (==, >, <, >=, <=, != )
#these operators will compare between two things
# and they will always produce a result in boolean

#Logical Operators
#(and, or, not)

print(12 == 12 and 56 == 56 and 34 > 78 and 12 > 10)
print(12 == 12 or 56 == 56 or 34 > 78 or 12 > 10)
# all the operations must be true
# if a single operation is false the final result
# is also going to be false 

# if any one of the operations is True 
# the whole result will be True 

print(not 12 == 12)
#it converts True to False and False to True

# control flow 
# (if else , Loops , Functions)

age = int(input("Apni age bata ! :- "))

if age >= 18:
    print("You can Vote.")

else:
    print("you cannot vote")