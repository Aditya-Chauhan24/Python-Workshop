# password=""
# while password!="12345":
#     password=input("enter your password:")
# print("access granted.")

# total=0
# for i in range(1,11):
#     total+=i
# print(total)

# name="Python"
# for letter in name:
#     print(letter)

# count=1
# while count<=5:
#     print(count)
#     count+=1

# cities=['new york','paris','tokyo']
# for city in cities:
#     print(city)

# for i in range (1,14):
#     for j in range(3,10):
#         if [i]==[j]:
#             print([i],[j])
        
# list1=[1,2,3,4,5,6,7,8]
# list2=[2,4,6,8,10,12]

# common_element=[]
# for element in list1:
#     if element in list2:
#         common_element.append(element)
# print("common element",common_element)

# for i in range(20):
#     if i > 10 and i % 4 == 0:
#         print(f"found:(i)")
#         break

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