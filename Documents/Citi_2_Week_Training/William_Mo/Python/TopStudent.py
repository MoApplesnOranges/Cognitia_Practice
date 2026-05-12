class Student:
    def __init__(self, student_id: int, name: str, grade: float):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def get_id(self):
        return self.student_id

    def get_name(self):
        return self.name

    def get_grade(self):
        return self.grade

    # Setters
    def set_id(self, student_id: int):
        self.student_id = student_id
    def set_name(self, name: str):
        self.name = name
    def set_grade(self, grade: float):
        self.grade = grade

    # display method
    def display(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Grade: {self.grade}")

def print_top_student(students):
    if not students:
        print("No students in the list.")
        return

    top_student = students[0]

    for student in students:
        if student.get_grade() > top_student.get_grade():
            top_student = student

    print("Top Student:")
    top_student.display()

# Main
if __name__ == "__main__":
    students = [
        Student(1, "Alice", 85.5),
        Student(2, "Bob", 92.0),
        Student(3, "Charlie", 78.0),
        Student(4, "David", 88.5)
    ]

    print_top_student(students)
