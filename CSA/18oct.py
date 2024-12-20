#18 oct 2024(list questions)
#assignment 

#Student Management System

courses = ["Python Programming", "RDBMS", "Web Technology", "Software Engg"]
electives = ["Business Intelligence", "Big Data Analytics"]

print("Number of courses opted by John:", len(courses))
print("Courses opted by John:", courses)

updated_courses = courses + electives
print("Updated courses with electives:", updated_courses)

if "Software Engg" in courses:
    courses[courses.index("Software Engg")] = "Computer Networks"
    print("Updated course list after change:", courses)
else:
    print("Course change not allowed as 'Software Engg' is not in the list.")

#Furniture Store Billing System

furniture = ["Sofa set", "Dining table", "T.V. Stand", "Cupboard"]
costs = [20000, 8500, 4599, 13920]

def calculate_bill(requested_items, quantities):
    bill_amount = 0
    #The zip() function returns a zip object, which is an iterator of tuples where the 
    #first item in each passed iterator is paired together, and then the second item in
    #each passed iterator are paired together 
    for item, quantity in zip(requested_items, quantities):
        if item in furniture and quantity > 0:
            index = furniture.index(item)
            cost = costs[index] * quantity
            bill_amount += cost
        else:
            print(f"Invalid request for item: {item} or invalid quantity.")
            return 0
    return bill_amount

requested_items = ["Sofa set", "Cupboard"]
quantities = [1, 2]
bill = calculate_bill(requested_items, quantities)
print("Total bill amount:", bill)

#Student Enrollment System (Java and Python Courses)

java_course = {"John", "Jack", "Jill", "Joe"}
python_course = {"Jake", "John", "Eric", "Jill"}

print("Number of students in Python course:", len(python_course))
print("Number of students in Java course:", len(java_course))

python_only = python_course - java_course
print("Students in Python course only:", python_only)

java_only = java_course - python_course
print("Students in Java course only:", java_only)

both_courses = java_course & python_course
print("Students in both Java and Python:", both_courses)

either_but_not_both = java_course ^ python_course
print("Students in either Java or Python but not both:", either_but_not_both)

either_course = java_course | python_course
print("Students in either Java or Python:", either_course)

#Customer Management System

customer_details = {1001: "John", 1004: "Jill", 1005: "Joe", 1003: "Jack"}

print("Customer Details:", customer_details)
print("Number of customers:", len(customer_details))

customer_details.pop(1005, None)
print("Updated customer details after deletion:", customer_details)

customer_details[1003] = "Mary"
print("Updated customer details after name change:", customer_details)


if 1002 in customer_details:
    print("Customer with ID 1002 exists.")
else:
    print("Customer with ID 1002 does not exist.")