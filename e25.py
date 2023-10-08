n=int(input("Donner un nombre : "))
while n<=0 :
    n=int(input("Donner un nombre positif non null: "))
f=1
for i in range(1,n+1):
    f = f * i
print("la factorielle est",f)