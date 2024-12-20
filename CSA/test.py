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