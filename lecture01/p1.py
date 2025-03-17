class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age

    def display_info(self):
        print("ID:", self.student_id, "/", "이름:", self.name, "/", "나이", self.age)

class StudentManager:
    def __init__(self): 
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)

    def display_all_students(self):
        for i in self.students:
            i.display_info()

info = StudentManager()
studentA = Student("1번", "김철수", "20살")
studentB = Student("2번", "이영희", "21살")
studentC = Student("3번", "박지민", "19살")
info.add_student(studentA)
info.add_student(studentB)
info.add_student(studentC)

print("현재 등록된 학생 목록:")
info.display_all_students()
print()

studentD = Student("4번", "한지수", "22살")
info.add_student(studentD)

print("학번 4번 추가 후:")
info.display_all_students()