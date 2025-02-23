import streamlit as st
import pandas as pd

# Title of the app
st.title("Student Data Manager")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Choose an action", ["Add Student", "View Students", "Update Student", "Delete Student"])

# Load or create a DataFrame to store student data
if 'students' not in st.session_state:
    st.session_state.students = pd.DataFrame(columns=["ID", "Name", "Age", "Grade"])

# Function to add a student
def add_student():
    st.subheader("Add a New Student")
    with st.form("add_student_form"):
        student_id = st.text_input("Student ID")
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0, max_value=100)
        grade = st.text_input("Grade")
        submitted = st.form_submit_button("Add Student")
        if submitted:
            new_student = pd.DataFrame([[student_id, name, age, grade]], columns=["ID", "Name", "Age", "Grade"])
            st.session_state.students = pd.concat([st.session_state.students, new_student], ignore_index=True)
            st.success("Student added successfully!")

# Function to view students
def view_students():
    st.subheader("View Students")
    st.write(st.session_state.students)

# Function to update a student
def update_student():
    st.subheader("Update Student Information")
    student_id = st.text_input("Enter Student ID to update")
    if student_id:
        student = st.session_state.students[st.session_state.students["ID"] == student_id]
        if not student.empty:
            st.write("Current Information:")
            st.write(student)
            with st.form("update_student_form"):
                name = st.text_input("Name", value=student.iloc[0]["Name"])
                age = st.number_input("Age", value=student.iloc[0]["Age"], min_value=0, max_value=100)
                grade = st.text_input("Grade", value=student.iloc[0]["Grade"])
                submitted = st.form_submit_button("Update Student")
                if submitted:
                    st.session_state.students.loc[st.session_state.students["ID"] == student_id, ["Name", "Age", "Grade"]] = [name, age, grade]
                    st.success("Student updated successfully!")
        else:
            st.error("Student ID not found!")

# Function to delete a student
def delete_student():
    st.subheader("Delete a Student")
    student_id = st.text_input("Enter Student ID to delete")
    if student_id:
        student = st.session_state.students[st.session_state.students["ID"] == student_id]
        if not student.empty:
            st.write("Student to be deleted:")
            st.write(student)
            if st.button("Confirm Delete"):
                st.session_state.students = st.session_state.students[st.session_state.students["ID"] != student_id]
                st.success("Student deleted successfully!")
        else:
            st.error("Student ID not found!")

# Navigation
if options == "Add Student":
    add_student()
elif options == "View Students":
    view_students()
elif options == "Update Student":
    update_student()
elif options == "Delete Student":
    delete_student()

# Display the current student data
st.subheader("Current Student Data")
st.write(st.session_state.students)