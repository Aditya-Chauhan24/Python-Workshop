# 16th oct 2024

#method 1
import sys

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
list_size = sys.getsizeof(list)
tuple_size = sys.getsizeof(tuple)
print(f"Memory size of list: {list_size} bytes")
print(f"Memory size oftuple: {tuple_size} bytes")

# flatten tuple
def flatten_tuple(nested_tuple):
    flat_list = []
    for item in nested_tuple:
        if isinstance(item, tuple):
            flat_list += flatten_tuple(item) #recursion
        else:
            flat_list.append(item) 
    return flat_list

nested_tuple = (1, (2, 3), (4, (5, 6)), 7)
flattened = flatten_tuple(nested_tuple)
print("Flattened tuple:", flattened)

#tuple sorting(Descending order):

students = (("Alice",88),("Bob",92),("Charlie",85))
def get_marks(student):
    return student[1]
sorted_students = sorted(students, key=get_marks, reverse=True)
sorted_students = tuple(sorted_students)

print(sorted_students)

#common element(tuple)

t1=(1,2,3,4,5)
t2=(4,5,6,7,8)
common=tuple(set(t1).intersection(t2))
print(common)

#append (tuple)

fruit=('apple','banana','cherry')
l_fruit=list(fruit)
l_fruit.append('orange')
fruit=tuple(l_fruit)
print(fruit)