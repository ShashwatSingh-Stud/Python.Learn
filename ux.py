# operators
# arithmetic (+,-,/,*,//,**,%)
# assignment
# comparision
# logical 

p = float(input("Principal = "))
r = float(input("rate = "))
t = float(input("Time = "))

SI = (p*r*t)//100
print(f"Your simple Interest is :{SI} ")

ci = p*(1+(r/100))**t

print(f"your CI will Be : {ci-p}")