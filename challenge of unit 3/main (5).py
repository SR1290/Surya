class student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_students(student_list):
  # sort the list of student in descending order in CGPA
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  # syntax
  return sorted_students


students = [
    student("Hari", "A123", 7.8),
    student("Srikanth", "A124", 8.9),
    student("Santhya", "A125", 9.1),
    student("Mohan", "A126", 9.9),
]

sorted_students = sort_students(students)

#print the list
for student in sorted_students:
  print("Name: {}, Roll No: {}, CGPA: {}".format(student.name,
                                                 student.roll_number,
                                                 student.cgpa))