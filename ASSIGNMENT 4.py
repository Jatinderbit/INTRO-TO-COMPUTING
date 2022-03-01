#QUESTION 1
def tower_hanoi(n,source,destination,auxillary):
    if n==1:
        print("move 1st disk from",source,"to",destination)
        return
    tower_hanoi(n-1,source,auxillary,destination)  #CALLING FUNCTION
    print("move",n,"th disk from",source,"to",destination)
    tower_hanoi(n-1,auxillary,destination,source)

n=3
tower_hanoi(n,"SOURCE","DESTINATION","AUXILLARY")


#QUESTION 2(IERATIVE METHOD)

n=int(input("ENTER THE ROW NUMBER:"))
lst=[]
for i in range(n):
    lst.append([])
    lst[i].append(1)
    for j in range(1,i):
        lst[i].append(lst[i-1][j-1]+lst[i-1][j])
    if(n!=0): #!= is defined as not equal to operator
        lst[i].append(1)
for i in range(n): # CREATING PATTERNS
    print("   "*(n-i),end=" ",sep=" ")
    for j in range(0,i+1):
        print('{0:6}'.format(lst[i][j]),end=" ",sep=" ")
    print()

#(RECURSUIVE METHOD)

def pscltri(n):
    if n==0:
        return[]
    elif n==1:
        return[[1]]
    else:
        new_row = [1]
        result = pscltri(n-1)
        last_row = result[-1]
        for i in range(len(last_row)-1):
            new_row.append(last_row[i]+last_row[i+1])
        new_row+=[1]
        result.append(new_row)
    return result
n=int(input("ENTER: "))
print(pscltri(n))

    
#QUESTION 3

#PART A
def value(a,b):
    quotient=a//b
    remainder=a%b
    print("THE QUOTIENT IS:",quotient)
    print("THE REMAINDER IS:",remainder)
    result= (quotient,remainder)
    return result

a = int(input("ENTER THE FIRST NUMBER: "))
b = int(input("ENTER THE SECOND NUMBER: "))
result=value(a,b)
print(result)

print("FUNCTION IS CALLABLE:",callable(value))
   
#PART B

print("a is zero:",a==0)
print("b is zero:",b==0)
print("quotient is zero:",result[0]==0)
print("remainder is zero:",result[1]==0)
if(a==0):
    print("a is zero")

#PART C
    
alist=[]
for i in result:
    if i>4:
        alist.append(i)
print("The values greater than 4 are:",alist)

#PART D

aset=set(alist)
print(aset)

#PART E

immutable_set=frozenset(aset)
print("The required immutable set",immutable_set)

#PART F

maxv=0
for i in immutable_set:
    if i>maxv:
        maxv=i
print("The required max value is:",maxv)
print("The required hash value is:",hash(maxv))
print("Done")

#QUESTION 4
class student:
    def __init__(self,nam,rollno):
        self.name=nam
        self.rollnumber= rollno
            
    def printdetails(self):
        print("NAME:",self.name)
        print("ROLL NUMBER:",self.rollnumber)

    def __del__(self):
        print("object that is created is destroyed")

data= student("JATINDER PAL SINGH",21104059)
print(data.name,",",data.rollnumber)


#QUESTION 5
class employee:
    count=0       
    def __init__(self,nam,sal):
        self.name=nam
        self.salary=sal
        employee.count=employee.count + 1

    def displaycount(self):
        print("The number of employees in the organization are: ", self.count)

    def displayemployee(self):
        print("NAME OF EMPLOYEE IS:",self.name)
        print("SALARY OF EMPLOYEE IS:",self.salary)
                   
e1 = employee("Mehak",40000)
e2 = employee("Ashok",50000)
e3 = employee("Viren",60000)

e1.displaycount()

e1.displayemployee()
e2.displayemployee()
e3.displayemployee()

#PART (a)
e3.salary=70000
print("UPDATED SALARY OF MEHAK IS:",e3.salary)

#PART (b)
del e3
print("Viren's record has been deleted")

#QUESTION 6
def anagram(word):
    if len(word)==1:
        return [word];
    partial_words=anagram(word[1:])
    char=word[0]
    mylist=[]
    for perm in partial_words:
        for i in range(len(perm)+1):
            mylist.append(perm[:i]+char+perm[i:])
    return mylist       


George_word=input("Gerorge's word:")
Possible_words=anagram(George_word)
Barbie_word=input("Barbie's word:")
print("Possible Words are:",Possible_words)
print("If Barbie's word is present in the list , then their friendship is real.")

if Barbie_word in Possible_words:
    print("Your Friendship is real.")
else:
    print("Your Friendship is fake.")
print("Done")






















     

        
        
    


















