# create employee class with id, name, salary, and department
# create a department class with deptID and name
# create a list of employee objects with sample employee data
# write method that takes list of employee objects and prints all items

class Department:
    def __init__(self, dept_id: int, name: str):
        self.dept_id = dept_id
        self.name = name

    def get_dept_id(self):
        return self.dept_id

    def get_name(self):
        return self.name

    def set_dept_id(self, dept_id: int):
        self.dept_id = dept_id

    def set_name(self, name: str):
        self.name = name

class Employee:
    def __init__(self, emp_id: int, name: str, salary: float, department: Department):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.department = department

    def get_id(self):
        return self.emp_id

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

    def get_department(self):
        return self.department.get_name()

    def get_department_id(self):
        return self.department.get_dept_id()

    def set_id(self, emp_id: int):
        self.emp_id = emp_id

    def set_name(self, name: str):
        self.name = name

    def set_salary(self, salary: float):
        self.salary = salary

    def set_department(self, department: Department):
        self.department = department

    def set_department_id(self, department: Department):
        self.department = department

hr = Department(1, "HR")
it = Department(2, "IT")
finance = Department(3, "Finance")

Employees = [
    Employee(1, "Alice", 50000, hr),
    Employee(2, "Bob", 60000, it),
    Employee(3, "Charlie", 55000, finance),
    Employee(4, "David", 70000, it),
    Employee(5, "Bill", 100000, it)
]

def print_employees(Employees):
    for emp in Employees:
        print(f"ID: {emp.get_id()}, Name: {emp.get_name()}, Salary: {emp.get_salary()}, Department_ID: {emp.get_department_id()}, Department: {emp.get_department()}" )

print_employees(Employees)
