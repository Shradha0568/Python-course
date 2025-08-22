import pandas as pd
import os
 
# CSV file name
FILE = "employees.csv"
 
# Initialize CSV if not exists
if not os.path.exists(FILE):
    df = pd.DataFrame(columns=["ID", "Name", "Age", "Department", "Role", "Salary"])
    df.to_csv(FILE, index=False)
 
# Function: Add Employee
def add_employee():
    df = pd.read_csv(FILE)
    try:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in df["ID"].values:
            print("Employee ID already exists!")
            return
 
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        dept = input("Enter Department: ")
        role = input("Enter Role: ")
        salary = float(input("Enter Salary: "))
 
        new_emp = pd.DataFrame([[emp_id, name, age, dept, role, salary]],
                               columns=df.columns)
        df = pd.concat([df, new_emp], ignore_index=True)
        df.to_csv(FILE, index=False)
        print("Employee added successfully.")
    except Exception as e:
        print("Error:", e)
 
# Function: View Employee
def view_employee():
    df = pd.read_csv(FILE)
    print("\n1. View by ID\n2. View by Department\n3. View All")
    choice = input("Enter choice: ")
 
    if choice == "1":
        emp_id = int(input("Enter Employee ID: "))
        result = df[df["ID"] == emp_id]
    elif choice == "2":
        dept = input("Enter Department: ")
        result = df[df["Department"].str.lower() == dept.lower()]
    else:
        result = df
 
    if result.empty:
        print("No records found.")
    else:
        print("\n---- Employee Details ----")
        print(result.to_string(index=False))
 
# Function: Update Employee
def update_employee():
    df = pd.read_csv(FILE)
    emp_id = int(input("Enter Employee ID to Update: "))
 
    if emp_id not in df["ID"].values:
        print("Employee not found.")
        return
 
    print("\n1. Update Role\n2. Update Department")
    choice = input("Enter choice: ")
 
    if choice == "1":
        new_role = input("Enter New Role: ")
        df.loc[df["ID"] == emp_id, "Role"] = new_role
    elif choice == "2":
        new_dept = input("Enter New Department: ")
        df.loc[df["ID"] == emp_id, "Department"] = new_dept
    else:
        print("Invalid choice")
        return
 
    df.to_csv(FILE, index=False)
    print("Employee updated successfully.")
 
# Function: Delete Employee
def delete_employee():
    df = pd.read_csv(FILE)
    emp_id = int(input("Enter Employee ID to Delete: "))
 
    if emp_id not in df["ID"].values:
        print("Employee not found.")
        return
 
    df = df[df["ID"] != emp_id]
    df.to_csv(FILE, index=False)
    print("Employee deleted successfully.")
 
# Main Menu
def main():
    while True:
        print("\n===== Employee Management System (CSV) =====")
        print("1. Add Employee")
        print("2. View Employee")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
 
        choice = input("Enter choice: ")
 
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employee()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            print("👋 Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
 
if __name__ == "__main__":
    main()