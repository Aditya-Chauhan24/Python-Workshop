#type of triangle
a=int(input("Enter the 1st side of triangle"))
b=int(input("Enter the 2nd side of triangle"))
c=int(input("Enter the 3rd side of triangle"))
if (a+b>c or b+c>a or a+c>b):
    print("Traingle is Valid")
    if (a==b and b==c and a==c):
        print("Equilateral Traingle")
    elif ((a==b) or (a==c) or (b==c)):
        print("Isosceles Triangle")
    else:
        print ("Scalene")
        
#employee salary
n=int(input("Enter your Salary:"))
y=int(input("Enter your year of service:"))
if (n>=50000 and y>=5):
    salary=n+(n*.10)
    print("Thank you! for being the part of our company for more than 5 years")
    print("This is your salary bonus")
    print(salary)
else:
    salary=n+(n*0.15)
    print("Thank you! for being the part of our company")
    print("This is your salary bonus")
    print(salary)
    
#eligiblity
person_is_eligible_to_vote=False
age_is_above_18=True
if(person_is_eligible_to_vote and age_is_above_18):
    print("you can vote")
else:
    print("you cannot vote")


#login
username=input("enter username")
password=input("enter password")
if username=="Admin" and password=="1234":
    print("Acess Granted")
else:
    print("Acess Denied")
    
#armstron number
number = int(input("Enter a number: "))

digits = str(number)
length= len(digits)

total = 0
for digit in digits:
    total += int(digit) ** length

if total == number:
    print("Armstrong number.")
else:
    print("not Armstrong number.")
    