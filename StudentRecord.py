import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Dictionary to store student records
students = {}

# Function to add a student
def add_student():
    student_id = entry_id.get()
    name = entry_name.get()
    age = entry_age.get()
    grade = entry_grade.get()
    
    if student_id and name and age and grade:
        students[student_id] = {'name': name, 'age': age, 'grade': grade}
        messagebox.showinfo("Success", "Student added successfully!")
        entry_id.delete(0, tk.END)
        entry_name.delete(0, tk.END)
        entry_age.delete(0, tk.END)
        entry_grade.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "All fields are required!")

# Function to view all students
def view_students():
    view_window = tk.Toplevel(root)
    view_window.title("Student Records")
    view_window.geometry("400x300")
    view_window.configure(bg="#ffcccb")
    
    if not students:
        tk.Label(view_window, text="No students found.", font=("Arial", 12), bg="#ffcccb").pack(pady=20)
    else:
        for student_id, data in students.items():
            tk.Label(view_window, text=f"ID: {student_id}, Name: {data['name']}, Age: {data['age']}, Grade: {data['grade']}", font=("Arial", 10), bg="#ffcccb").pack(anchor='w', padx=10)

# Function to search for a student
def search_student():
    student_id = entry_id.get()
    if student_id in students:
        data = students[student_id]
        messagebox.showinfo("Student Found", f"ID: {student_id}\nName: {data['name']}\nAge: {data['age']}\nGrade: {data['grade']}")
    else:
        messagebox.showerror("Error", "Student not found!")

# Function to update student details
def update_student():
    student_id = entry_id.get()
    if student_id in students:
        students[student_id] = {'name': entry_name.get(), 'age': entry_age.get(), 'grade': entry_grade.get()}
        messagebox.showinfo("Success", "Student updated successfully!")
    else:
        messagebox.showerror("Error", "Student not found!")

# Function to delete a student
def delete_student():
    student_id = entry_id.get()
    if student_id in students:
        del students[student_id]
        messagebox.showinfo("Success", "Student deleted successfully!")
    else:
        messagebox.showerror("Error", "Student not found!")

# Main Window
root = tk.Tk()
root.title("Student Management System")
root.geometry("500x500")
root.configure(bg="#dbeeff")

# Title Label
title_label = tk.Label(root, text="Student Management System", font=("Helvetica", 16, "bold"), fg="white", bg="#007acc")
title_label.pack(fill=tk.X, pady=10)

# Form Frame
form_frame = tk.Frame(root, bg="#f0f8ff")
form_frame.pack(pady=20)

# Labels and Entry Fields
fields = ["Student ID", "Name", "Age", "Grade"]
entries = []
for i, field in enumerate(fields):
    tk.Label(form_frame, text=field, font=("Arial", 12, "bold"), bg="#f0f8ff").grid(row=i, column=0, padx=10, pady=5)
    entry = tk.Entry(form_frame, font=("Arial", 12))
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

entry_id, entry_name, entry_age, entry_grade = entries

# Buttons with styling
btn_frame = tk.Frame(root, bg="#dbeeff")
btn_frame.pack(pady=20)

tk.Button(btn_frame, text="Add Student", command=add_student, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white").grid(row=0, column=0, padx=10, pady=5)
tk.Button(btn_frame, text="View Students", command=view_students, font=("Arial", 12, "bold"), bg="#2196F3", fg="white").grid(row=0, column=1, padx=10, pady=5)
tk.Button(btn_frame, text="Search", command=search_student, font=("Arial", 12, "bold"), bg="#FF9800", fg="white").grid(row=0, column=2, padx=10, pady=5)
tk.Button(btn_frame, text="Update", command=update_student, font=("Arial", 12, "bold"), bg="#FFC107", fg="black").grid(row=1, column=0, padx=10, pady=5)
tk.Button(btn_frame, text="Delete", command=delete_student, font=("Arial", 12, "bold"), bg="#F44336", fg="white").grid(row=1, column=1, padx=10, pady=5)
tk.Button(btn_frame, text="Exit", command=root.quit, font=("Arial", 12, "bold"), bg="#9E9E9E", fg="white").grid(row=1, column=2, padx=10, pady=5)

root.mainloop()
