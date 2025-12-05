import re
import os  # for cls command

class Student:
    def __init__(self, student_id, name, email, age):
        self.student_id = student_id
        self.name = name
        # Task 6: Encapsulation (Private Attributes)
        self.__email = None 
        self.__age = None   
        
        # Use setters to initialize private variables with validation
        self.set_email(email)
        self.set_age(age)

    # --- Getters and Setters ---

    def get_email(self):
        return self.__email

    # Task 2: Validate Email Format inside Setter
    def set_email(self, email):
        # Clean the input first
        email = email.strip()
        
        # Specific Error Trapping: Check if '@' is missing
        if "@" not in email:
            print(f"   [!] Error: Invalid email '{email}'. Missing '@' symbol.")
            self.__email = None
            return

        # Regex to check valid email format (Standard validation)
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if re.match(email_pattern, email):
            self.__email = email
        else:
            print(f"   [!] Error: Invalid email format '{email}'. Check for invalid characters or missing domain.")
            self.__email = None

    def get_age(self):
        return self.__age

    def set_age(self, age):
        try:
            self.__age = int(age)
        except ValueError:
            print(f"   [!] Error: Invalid age '{age}'. Must be a number.")
            self.__age = 0

    # Task 3: Replace Sensitive Info (Masking)
    def get_masked_email(self):
        if self.__email:
            # Replaces the username part before @ with *****
            return re.sub(r"^[\w\.-]+", "*****", self.__email)
        return "N/A"

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name:      {self.name}")
        print(f"Email:     {self.get_email()} (Masked: {self.get_masked_email()})")
        print(f"Age:       {self.get_age()}")

# Task 8: Inheritance
class Scholar(Student):
    def __init__(self, student_id, name, email, age, scholarship_type):
        super().__init__(student_id, name, email, age)
        self.scholarship_type = scholarship_type

    def display_scholar_info(self):
        self.display_info() # Reuse parent method
        print(f"Scholarship: {self.scholarship_type}")


# ==========================================
# PART 1: REGULAR EXPRESSION TASKS (Logic)
# ==========================================

def extract_student_data(raw_input):
    """
    Task 1: Extract Student Data Using Regex with Named Groups
    Improved Input Format: "2025-001 | Juan Dela Cruz | juan@test.com | 20"
    No need to type keys like ID:, Name:, etc.
    """
    # Improvement: Expects 4 fields separated by |
    # NOTE: Changed email pattern to (?P<email>[^|]+) to allow 'bad' emails 
    # to pass through so the Student class can handle the specific error message.
    pattern = r"^\s*(?P<id>[\w-]+)\s*\|\s*(?P<name>[a-zA-Z\s]+)\s*\|\s*(?P<email>[^|]+)\s*\|\s*(?P<age>\d+)\s*$"
    
    match = re.search(pattern, raw_input)
    
    if match:
        data = match.groupdict()
        # Clean up whitespace captured by the relaxed regex
        data['email'] = data['email'].strip()
        data['name'] = data['name'].strip()
        return data
    else:
        return None

def clear_screen():
    """Clears the console screen based on OS."""
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

# ==========================================
# PART 3: INTEGRATION TASK (Main System)
# ==========================================

def main():
    student_records = []

    while True:
        clear_screen() # Clear screen before showing menu
        print("\n" + "="*50)
        print(" STUDENT INFORMATION PROCESSING SYSTEM ")
        print("="*50)
        print("1. Add Regular Student")
        print("2. Add Scholar")
        print("3. View All Records")
        print("4. Exit")
        print("-" * 50)
        
        choice = input("Select an option (1-4): ")

        if choice == '1' or choice == '2':
            print("\n--- ENTER RAW DATA ---")
            print("Format:  <ID> | <Name> | <Email> | <Age>")
            print("Example: 2025-001 | Juan Cruz | juan@gmail.com | 20")
            
            raw_data = input("\n Enter Here: ")
            
            # Extract data using Regex
            data = extract_student_data(raw_data)
            
            if data:
                # Task 4: Find All Words in Name (Cleaning extra spaces)
                name_words = re.findall(r"[A-Za-z]+", data['name'])
                clean_name = " ".join(name_words)

                if choice == '1':
                    # Create Student Object
                    new_student = Student(data['id'], clean_name, data['email'], data['age'])
                    
                    # Validation Check: Only add if email is valid
                    if new_student.get_email(): 
                        student_records.append(new_student)
                        print("\n[+] Student successfully added!")
                    else:
                        print("\n[X] Record NOT added. Please fix the email format.")
                
                elif choice == '2':
                    scholarship = input("Enter Scholarship Type (e.g., Academic, Athletic): ")
                    # Create Scholar Object
                    new_scholar = Scholar(data['id'], clean_name, data['email'], data['age'], scholarship)
                    
                    # Validation Check
                    if new_scholar.get_email():
                        student_records.append(new_scholar)
                        print("\n[+] Scholar successfully added!")
                    else:
                        print("\n[X] Record NOT added. Please fix the email format.")

            else:
                print("\n[!] ERROR: Format doesn't match! Please ensure you use '|' to separate values.")
                print("Correct Example: 2023-123 | Mario Bros | mario@nintendo.com | 25")
            
            # Pause so user can see the result before screen clears
            input("\nPress Enter to return to menu...")

        elif choice == '3':
            print("\n" + "="*20 + " ALL RECORDS " + "="*20)
            if not student_records:
                print("No records found.")
            else:
                for i, student in enumerate(student_records, 1):
                    print(f"\n[Record #{i}]")
                    if isinstance(student, Scholar):
                        student.display_scholar_info()
                    else:
                        student.display_info()
                    print("-" * 40)
            input("\nPress Enter to continue...")

        elif choice == '4':
            print("\nExiting system... Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()