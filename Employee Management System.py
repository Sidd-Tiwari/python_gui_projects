"""
A class to create a graphical user interface for an Employee Management System using Tkinter.
"""

import tkinter as tk
from tkinter import messagebox

class Employee:
    def __init__(self, name, designation, emp_id):
        self.name = name
        self.designation = designation
        self.emp_id = emp_id

class EmployeeManagement:
    def __init__(self):
        self.employees = []
    
    def add_employee(self, name, designation, emp_id):
        employee = Employee(name, designation, emp_id)
        self.employees.append(employee)
    
    def display_employees(self):
        if not self.employees:
            return "No employees available."
        
        catalog = "\nEmployee List:\n"
        for emp in self.employees:
            catalog += f"Name: {emp.name}, Designation: {emp.designation}, Employee ID: {emp.emp_id}\n"
        return catalog
    
    def search_employee(self, emp_id):
        for emp in self.employees:
            if emp_id == emp.emp_id:
                return f"Name: {emp.name}, Designation: {emp.designation}, Employee ID: {emp.emp_id}"
        return f"Employee with ID '{emp_id}' not found."

class EmployeeGUI:
    
    def __init__(self, root):
        self.management = EmployeeManagement()
        self.root = root
        self.root.title("Employee Management System")
        
        self.create_widgets()
    
    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Employee Management System", font=("Helvetica", 16))
        self.title_label.pack(pady=10)
        
        self.add_button = tk.Button(self.root, text="Add Employee", command=self.add_employee, font=("Helvetica", 14))
        self.add_button.pack(pady=5)
        
        self.display_button = tk.Button(self.root, text="Display Employees", command=self.display_employees, font=("Helvetica", 14))
        self.display_button.pack(pady=5)
        
        self.search_button = tk.Button(self.root, text="Search Employee", command=self.search_employee, font=("Helvetica", 14))
        self.search_button.pack(pady=5)
        
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit, font=("Helvetica", 14))
        self.exit_button.pack(pady=5)
    
    def add_employee(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Add Employee")
        
        self.name_label = tk.Label(self.new_window, text="Name:")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(self.new_window)
        self.name_entry.pack(pady=5)
        
        self.designation_label = tk.Label(self.new_window, text="Designation:")
        self.designation_label.pack(pady=5)
        self.designation_entry = tk.Entry(self.new_window)
        self.designation_entry.pack(pady=5)
        
        self.emp_id_label = tk.Label(self.new_window, text="Employee ID:")
        self.emp_id_label.pack(pady=5)
        self.emp_id_entry = tk.Entry(self.new_window)
        self.emp_id_entry.pack(pady=5)
        
        self.add_button = tk.Button(self.new_window, text="Add Employee", command=self.add_employee_to_system)
        self.add_button.pack(pady=10)
    
    def add_employee_to_system(self):
        name = self.name_entry.get()
        designation = self.designation_entry.get()
        emp_id = self.emp_id_entry.get()
        self.management.add_employee(name, designation, emp_id)
        messagebox.showinfo("Success", f"Employee '{name}' has been added.")
        self.new_window.destroy()
    
    def display_employees(self):
        employees = self.management.display_employees()
        messagebox.showinfo("Employee List", employees)
    
    def search_employee(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Search Employee")
        
        self.search_label = tk.Label(self.new_window, text="Employee ID:")
        self.search_label.pack(pady=5)
        self.search_entry = tk.Entry(self.new_window)
        self.search_entry.pack(pady=5)
        
        self.search_button = tk.Button(self.new_window, text="Search", command=self.search_employee_in_system)
        self.search_button.pack(pady=10)
    
    def search_employee_in_system(self):
        emp_id = self.search_entry.get()
        result = self.management.search_employee(emp_id)
        messagebox.showinfo("Search Result", result)
        self.new_window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeGUI(root)
    root.mainloop()
