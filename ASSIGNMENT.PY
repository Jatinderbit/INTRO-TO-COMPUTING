#ASSIGNMENT 1
#QUESTION 1
print("AVERAGE OF THREE NUMBERS" "\n")

number1 = int(input(" number1 ="))
number2 = int(input(" number2 ="))
number3 = int(input(" number3 ="))
average =float((number1 + number2 + number3)/3)
print (average)



#QUESTION 2
print("INCOME TAX" "\n")
Grossincome= int(input("enter the Gross income(y) = $ "))
dep = int(input("Number of dependents = "))

Taxable_income = Grossincome-10000-3000*dep
TAX = Taxable_income*20/100
#tax rate is 20%
print(TAX)


#QUESTION 3
print("STUDENT DATA" "\n")
Name = input("Student Name " )
SID = input("enter SID ")
Gender = input("enter Gender ")
Coursename = input("Course Name ")
CGPA =float(input('CGPA')) 
student=[Name, SID, Gender, Coursename, CGPA]
print(student)


#QUESTION 4
print("MARKS OF 5 STUDENTS" "\n")

student1= int(input("Marks of student1 = "))

student2= int(input("Marks of student2 = "))

student3= int(input("Marks of student3 = "))

student4= int(input("Marks of student4 = "))

student5= int(input("Marks of student5 = "))

Sorted_Marks = [student1,student2,student3,student4,student5]
print(Sorted_Marks)


#QUESTION 5(a)
print("COLOR" "\n")

color = ['Red','Green','White','Black','Pink','Yellow']
color.remove('Black')
print(color)
 
#QUESTION 5(b)
color = ['Red','Green','White','Black','Pink','Yellow']
color.remove('Black')
color.remove('Pink')
color.insert (3, 'Purple')
print(color)

