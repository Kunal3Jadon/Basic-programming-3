#1.. WAP to Sort three integers without using conditional statements and loops
x=int(input())
y=int(input())
z=int(input())
a1=min(x,y,z)
a3=max(x,y,z)
a2=(x+y+z)-a1-a3
print(a1,a2,a3)
#2..WAP to Calculate Body Mass Index
height=float(input())
weight=float(input())
bmi = weight/(height**2)
print(bmi)
#3..WAP to print ASCII value of a caracter
c=input()
print(ord(c))
#4..WAP to calculate sum of numbers given in single line input
r=eval(input())
print(r)
