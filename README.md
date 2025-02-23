# Student Data Manager

The Student Data Manager is a Streamlit-based web application that allows users to perform various operations on student data, including adding, viewing, updating, and deleting student information. The application uses an in-memory pandas DataFrame to store and manage the student data.

# Features

Add Student: Allows the user to add a new student by providing their ID, Name, Age, and Grade.
View Students: Displays all the current student data in a tabular format.
Update Student: Lets the user update the information of a specific student by providing their ID.
Delete Student: Allows the user to delete a student record by providing their ID.

# Prerequisites

Python 3.x
Streamlit
Pandas

## You can install the required dependencies by running:
```
pip install streamlit pandas
```
## How to Run the Application

Clone or download the project files.
Open a terminal in the project folder.
Run the Streamlit app using the following command:

```
streamlit run app.py
```

Replace ``app.py`` with the name of the script if it's different.

The app will open in your default web browser, and you can interact with it to manage student data.

# Application Workflow
## Sidebar Navigation: The sidebar allows users to choose between different actions:

"Add Student" to add a new student.
"View Students" to view all current students.
"Update Student" to update a student's information by their ID.

## Student Data Storage:

The student data is stored in a pandas DataFrame, which is saved in the session state to persist data across app interactions.
The columns for student information are ID, Name, Age, and Grade
"Delete Student" to delete a student's record by their ID.

##  How it Works

Add Student:
The user enters the student's ID, name, age, and grade and clicks the "Add Student" button.
The new student's data is appended to the existing student DataFrame.
A success message is displayed after the addition.

## View Students:
Displays a table of all the students' information stored in the DataFrame.

## Update Student:
The user enters the student's ID they wish to update.
If the student is found, their current information is displayed, and the user can modify the details (Name, Age, Grade).
After submitting the updated information, the student data is updated in the DataFrame, and a success message is displayed.

## Delete Student:
The user enters the student's ID they want to delete.
If the student is found, their details are shown, and the user can confirm deletion.
Once confirmed, the student is removed from the DataFrame, and a success message is displayed.

## Example of Data

| ID   | Name    | Age | Grade |
|------|---------|-----|-------|
| 101  | Alice   | 20  | A     |
| 102  | Bob     | 22  | B     |
| 103  | Charlie | 21  | A     |


This README should help others understand and use your Streamlit app. Let me know if you'd like any changes!
