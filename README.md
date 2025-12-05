Student Information Processing System

A Python-based console application designed to demonstrate Object-Oriented Programming (OOP) and Regular Expressions (Regex). The system processes raw student data strings, validates input, and stores records using encapsulation and inheritance.

Features

Regex Extraction: Automatically parses raw text strings to extract ID, Name, Email, and Age.

Data Validation:

Ensures email format is valid (must contain @ and domain).

Ensures age is a valid number.

OOP Principles:

Encapsulation: Uses private attributes (__email, __age) accessed via getters and setters.

Inheritance: Scholar class inherits from the Student base class.

Privacy: Displays masked emails (e.g., *****@gmail.com) in the records view.

Interactive Menu: Clean interface with error trapping and screen clearing.

How to Run

Ensure you have Python installed.

Run the script in your terminal:

python student_system.py


Usage

Adding a Student

Select option 1 (Student) or 2 (Scholar). The program will ask for Raw Data. You must enter the data in the following pipe-separated format:

<ID> | <Name> | <Email> | <Age>

Example Input:

2025-001 | Juan Dela Cruz | juan@example.com | 20


Note: If the email is invalid (missing @ or invalid characters), the system will reject the entry and display an error message.

Viewing Records

Select option 3 to view all stored students. This will display:

Student ID

Name (cleaned of extra spaces)

Email (Masked for privacy)

Age

Scholarship Type (if applicable)

Requirements

Python 3.x

Standard libraries: re, os (no external installations needed)
