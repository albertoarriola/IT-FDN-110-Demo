# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This lab demonstrates using input and output to a file
# Change Log: (Who, When, When)
#   Alberto Arriola, 2/12/2025, Created script
# ------------------------------------------------------------------------------------------ #


# Constants
MENU: str = """---- Course Registration Program ----
  Select from the following menu:
   1. Register a student for a courses
   2. Show current data
   3. Save data to a file
   4. Exit the program
-------------------------------------"""                    # String constant containing the Menu with choices for the user
FILE_NAME: str = "Enrollments.json"                         # String constant containing the name of the external .json file

# Variables
student_first_name: str = " "                               # String variable containing the student's first name
student_last_name: str = " "                                # String variable containing the student's last name
course_name: str = " "                                      # String variable containing the course name
json_data: str = " "                                        # String variable containing data to be uploaded to the external json file
file: object = None                                         # Object variable for external file
menu_choice: str = " "                                      # String variable containing the user's menu selection
student_data: dict[str, str] = {}                           # Dictionary variable for collecting entered student information
students: list = []                                         # List variable for collecting all the entered student information
student_data_exists: bool = False                           # Boolean variable to track whether student data has been uploaded or recorded

import json                                                                                     # import json module

# open json file
try:                                                                                            # try statement for exception handling
    file = open(FILE_NAME, "r")                                                                 # External json file is opened with 'r' read argument, named 'Enrollments.csv' and assigned to the file Object variable
except FileNotFoundError as e:                                                                  # except statement catches FileNotFoundError
    print(f"File \"{FILE_NAME}\" does not exist.\n")                                            # Print out custom statement stating that the external file does not exist
    print("Built-In Python error info: ")                                                       # Print out a header for the built-in Python error messages
    print(e, e.__doc__, type(e), sep='\n')                                                      # Print out value for 'e', documentation for File Not Found error, and error class
else:                                                                                           # else statement executed if except statement is not triggered
    students = json.load(file)                                                                  # Contents of file is loaded into the students List variable using the json.load() function
    file.close()                                                                                # External json file is closed
    student_data_exists = True                                                                  # student_data_exists Boolean variable is set to True if external file with student data exists

while (True):                                                                                   # while loop starts so that the program runs until the user chooses to exit

    print()                                                                                     # Extra print() line for formatting
    print(MENU)                                                                                 # Menu string is printed out to offer choices to the user
    print()                                                                                     # Extra print() line for formatting
    menu_choice = input("Please make a selection: ")                                            # input() asks user to make a menu selection and assigns it to the menu_choice string variable

# Selection 1. Register a student for a course
    if (menu_choice == "1"):                                                                    # if statement triggered when user enters "1" from the menu
        while True:                                                                             # while Loop continues to execute if the user enters a first name with a number
            try:                                                                                # try statement for exception handling
                student_first_name = input("Enter the student's first name: ")                  # input() asks user to enter student's first name and assigns answer to student_first_name string variable
                if not student_first_name.isalpha():                                            # if statement checking if student's first name contains numbers
                    raise Exception("The student's first name should only contain letters.")    # Exception message for when student's first name contains numbers
            except Exception as e:                                                              # Exception is thrown if student's first name contains numbers
                print(e)                                                                        # Print e; Exception message
                print()                                                                         # Extra print() line for formatting
                continue                                                                        # continue statement returns user to start of while Loop to enter student's first name again
            else:                                                                               # else statement is triggered when user enters a student's first name without any numbers
                break                                                                           # code breaks out of while Loop when user enters a student's first name without any numbers

        while True:                                                                             # while Loop continues to execute if the user enters a last name with a number
            try:                                                                                # try statement for exception handling
                student_last_name = input("Enter the student's last name: ")                    # input() asks user to enter student's last name and assigns answer to student_last_name string variable
                if not student_last_name.isalpha():                                             # if statement checking if student's last name contains numbers
                    raise Exception("The student's last name should only contain letters.")     # Exception message for when student's first name contains numbers
            except Exception as e:                                                              # Exception is thrown if student's first name contains numbers
                print(e)                                                                        # Print e; Exception message
                print()                                                                         # Extra print() line for formatting
                continue                                                                        # continue statement returns user to start of while Loop to enter student's last name again
            else:                                                                               # else statement is triggered when user enters a student's last name without any numbers
                break                                                                           # code breaks out of while Loop when user enters a student's first name without any numbers

        course_name = input("Enter the course name: ")                                          # input() asks user to enter course name and assigns answer to course_name string variable
        student_data = {"FirstName":student_first_name,
                        "LastName":student_last_name,
                        "CourseName":course_name}                                               # student_first_name, student_last_name, course_name KeyName Value pairs added to the student_data dictionary
        students.append(student_data)                                                           # contents of student_data Dictionary variable is appended to students List variable
        student_data_exists = True                                                              # student_data_exists boolean variable is set to 'True' because student data has been recorded
        print()                                                                                 # Extra print() line for formatting
        continue                                                                                # continue statement returns the user to the start of the while loop

# Selection 2. Show current data
    elif (menu_choice == "2"):                                                                  # elif statement triggered when user enters "2" from the menu                                                                                          # else statement for nested if statement triggered if student_data boolean variable is 'True' meaning student data has been recorded
        if student_data_exists == False:                                                        # Nested if statement triggered if student_data_exists boolean variable is 'False' meaning no student data has been recorded
            print("There is no student data to display.")                                       # User is notified that no student data exists to be displayed
        else:                                                                                   # else statement for nested if statement triggered if student_data_exists boolean variable is 'True' meaning student data has been recorded
            print()                                                                             # Extra print() line for formatting
            print("The current data is: ")                                                      # Header is printed to notify user of the current student registration data
            for student in students:                                                            # Nested for loop iterates for each student item in the students List variable
                print(student["FirstName"], student["LastName"]
                      + ", " + student["CourseName"])                                           # Each student in the students List variable is printed out
            print()                                                                             # Extra print() line for formatting
            continue                                                                            # continue statement returns the user to the start of the while loop

# Selection 3. Save data to a file
    elif (menu_choice == "3"):                                                                  # elif statement triggered when user enters "3" from the menu                                                                                          # else statement for nested if statement triggered if student_data boolean variable is 'True' meaning student data has been recorded
        if student_data_exists == False:                                                        # Nested if statement triggered if student_data_exists boolean variable is 'False' meaning no student data has been recorded
            print("There is no student data to upload.")                                        # User is notified that no student data exists to be uploaded
        else:                                                                                   # else statement for nested if statement triggered if student_data_exists boolean variable is 'True' meaning student data has been recorded
            file = open(FILE_NAME, "w")                                                         # External json file is opened with 'w' write argument, named 'Enrollments.csv' and assigned to the file Object variable
            try:
                json.dump(studen1, file)                                                        # json.dump function is used to upload contents of students List file to external json file
            except NameError as e:
                print("Built-In Python error info: ")
                print(e, e.__doc__, type(e), sep='\n')
                print()
            json.dump(students, file)
            file.close()                                                                        # External json file is closed
            for student in students:                                                            # Nested for loop iterates for each student item in the students List variable
                print(f"{student["FirstName"]} {student["LastName"]} has "
                        f"been registered for {student["CourseName"]}.")                        # F string is used to format printout of first name, last name and course name
            print()                                                                             # Extra print() line for formatting
            continue                                                                            # continue statement returns the user to the start of the while loop

# Selection 4. Exit the program
    elif (menu_choice == "4"):                                                                  # elif statement triggered when user enters "4" from the menu
        print("Goodbye!")                                                                       # print() 'Goodbye!'
        break                                                                                   # break statement stops the while loop and ends the program

# Invalid selection
    else:                                                                                       # final else statement triggered if user enters anything other than "1", "2", "3", or "4" from the menu
        print(menu_choice + " is not a valid selection.")                                       # print() tells user that their selection is invalid
        print()                                                                                 # Extra print() line for formatting
        continue                                                                                # continue statement returns the user to the start of the while loop