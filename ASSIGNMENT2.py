#QUESTION 1

print("QUESTION 1:\n") 
x= "Python is a case sensitive language"
print(len(x))
k=x[::-1]#reverse the string 
print(k)
print(x[9:27])
y=x.replace('a case sensitive','object oriented')# or we can us mystr.replace("","") 
print(y)
u=x.index("a")# find the index of a
print(u) 
t = x.replace(' ','')
print(t)

#QUESTION 2

print("QUESTION 2:\n") 
n ="Jatinder Pal Singh"
x = 21104059
dep= "Electrical Engineering"
y= 9.9
a=f" Hey, {n} here!" #f means fast.It helps in fast String formatting 
print(a)
b=f" My SID is {x}"
print(b)
t=f" Iam from {dep} department and my CGPA is {y}"
print(t)

#QUESTION 3

print("QUESTION 3:\n") 
a=56
b=10
print(a&b)

print(a|b)

print(a^b)

print(a<<2)

print(b<<2)

print(a>>2)

print(b>>4)


#QUESTION 4

print("QUESTION 4:\n")
n1=int(input("enter number 1: "))
n2=int(input("enter number 2: "))
n3=int(input("enter number 3: "))
       
if (n1>n2)and(n1>n3):
       print("n1 is greatest")
       
elif (n2>n1)and(n2>n3):
    print("n2 is gratest")
else:
    print("n3 is greatest")

    
#QUESTION 5
    
print("QUESTION 5:\n")
sentence=input("TYPE ANY SENTENCE:\n")
search_character="name"

if(search_character in sentence):
    print("YES")
#in keyword is used to check if a value is present in a sequence     
else:
   print("NO")
   

#QUESTION 6

print("QUESTION 6:\n")
x=int(input("LENGTH 1 : "))
y=int(input("LENGTH 2 : "))
z=int(input("LENGTH 3 : "))
if x>(y+z) or y>(x+z) or z>(x+y):
    print("NO")
else:
     print("YES")
    
      


























