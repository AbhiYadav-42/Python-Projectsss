class School:
    def __init__(self, name, address, code):
        self.school_name = name
        self.school_address = address
        self.school_code = code
        self.students = []  


class Student:
    def __init__(self, name, roll_no, clas):
        self.name = name
        self.roll_no = roll_no
        self.clas = clas 
        self.subjects = ["Maths", "Science", "English", "Hindi", "SST"]
        self.attendance_record = {subject: "" for subject in self.subjects}
        self.result_record = {subject: None for subject in self.subjects}

    def add_subjects(self, subjects):
        self.subjects = subjects

    def mark_attendance(self, subject, percentage):
        self.attendance_record[subject] = percentage

    def add_result(self, subject, marks):
        self.result_record[subject] = marks


class Admin:
    def add_student(self, school, student_obj):
        school.students.append(student_obj)

    def remove_student(self, school, roll_no):
        school.students = [s for s in school.students if s.roll_no != roll_no]

    def count_students(self, school):
        return len(school.students)


# -----------------------------
# 💡 Execution starts here:
# -----------------------------

my_school = School("Green Valley", "New Delhi", "GV001")
print(f"Welcome to {my_school.school_name}, {my_school.school_address}")
print(f"School unique code: {my_school.school_code}")

admin = Admin()

s2 = Student("Riya", 102, "9th")

admin.add_student(my_school, s2)

print("Total Students:", admin.count_students(my_school))
