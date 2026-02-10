import os

class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id},{self.name},{self.department},{self.salary}"


class EmployeeManager:
    file_name = "employees.txt"

    @staticmethod
    def add_employee():
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        salary = input("Enter Salary: ")

        employee = Employee(emp_id, name, department, salary)

        with open(EmployeeManager.file_name, "a") as file:
            file.write(str(employee) + "\n")

        print("✅ Employee added successfully!\n")

    @staticmethod
    def view_employees():
        if not os.path.exists(EmployeeManager.file_name):
            print("⚠ No records found.\n")
            return

        print("\n--- Employee Records ---")
        with open(EmployeeManager.file_name, "r") as file:
            records = file.readlines()
            if not records:
                print("No employees found.\n")
                return

            for record in records:
                emp_id, name, department, salary = record.strip().split(",")
                print(f"ID: {emp_id} | Name: {name} | Dept: {department} | Salary: {salary}")
        print()

    @staticmethod
    def search_employee():
        search_id = input("Enter Employee ID to search: ")
        found = False

        if not os.path.exists(EmployeeManager.file_name):
            print("⚠ No records found.\n")
            return

        with open(EmployeeManager.file_name, "r") as file:
            for record in file:
                emp_id, name, department, salary = record.strip().split(",")
                if emp_id == search_id:
                    print("\n✅ Employee Found:")
                    print(f"ID: {emp_id} | Name: {name} | Dept: {department} | Salary: {salary}\n")
                    found = True
                    break

        if not found:
            print("❌ Employee not found.\n")

    @staticmethod
    def delete_employee():
        delete_id = input("Enter Employee ID to delete: ")
        found = False

        if not os.path.exists(EmployeeManager.file_name):
            print("⚠ No records found.\n")
            return

        with open(EmployeeManager.file_name, "r") as file:
            records = file.readlines()

        with open(EmployeeManager.file_name, "w") as file:
            for record in records:
                emp_id = record.strip().split(",")[0]
                if emp_id != delete_id:
                    file.write(record)
                else:
                    found = True

        if found:
            print("🗑 Employee deleted successfully!\n")
        else:
            print("❌ Employee not found.\n")


def menu():
    while True:
        print("====== Employee Record Management System ======")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            EmployeeManager.add_employee()
        elif choice == "2":
            EmployeeManager.view_employees()
        elif choice == "3":
            EmployeeManager.search_employee()
        elif choice == "4":
            EmployeeManager.delete_employee()
        elif choice == "5":
            print("👋 Exiting system. Goodbye!")
            break
        else:
            print("⚠ Invalid choice, try again.\n")


if __name__ == "__main__":
    menu()