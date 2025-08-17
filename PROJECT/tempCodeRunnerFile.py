s2 = Student("Riya", 102, "9th")

# Admin adds students to school

admin.add_student(my_school, s2)

# Check student count
print("Total Students:", admin.count_students(my_school))