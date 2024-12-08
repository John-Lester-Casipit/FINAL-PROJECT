name=input("enter a name:")
amount=eval(input("enter amount to deposit:"))


a1=amount//1000
a2=amount%1000

b1=a2//500
b2=a2%500

c1=b2//200
c2=b2%200

d1=c2//100
d2=c2%100

e1=d2//50
e2=d2%50

f1=e2//20
f2=e2%20

g1=f2//10
g2=f2%10

h1=g2//5
h2=g2%5

i1=h2//1
i2=h2%1

print("Hi,",name,"The breakdown of your deposit",amount,"is:")
print("1,000--",a1,)
print("  500--",b1,)
print("  200--",c1,)
print("  100--",d1,)
print("   50--",e1,)
print("   20--",f1,)
print("   10--",g1,)
print("    5--",h1,)
print("    1--",i1,)