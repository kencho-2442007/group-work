# Lab03_3.py
# We need to figure out the logic to collect all the students. Specifically we are looking for students with IDs that end in 6 or 7. 
# So the logic should find all the students with IDs that have 6 or 7 at the end. We are focusing on students, with IDs ending in 6 or 7.

import csv

def main():
    # Names of the files we are working with
    input_file = "students.txt"
    output_file = "group_3.txt"
    
    # This list will store all students who meet our condition
    group_3_list = []

    try:
        # 1. Open the file using the CSV library
        with open(input_file, mode='r') as file:
            # csv.reader automatically separates the Name and ID
            reader = csv.reader(file)
            
            serial = 1  # Start serial number from 1
            for row in reader:
                # Basic check to make sure the row has data (Name and ID)
                if len(row) == 2:
                    # Add serial number to make it [Serial, Name, ID]
                    full_row = [str(serial), row[0], row[1]]
                    # row[2] is the Student ID column (now full_row[2])
                    student_id = full_row[2]
                    
                    # 2. Logic to "add" student to our group list
                    # We check the last character of the ID string
                    if student_id[-1] == '6' or student_id[-1] == '7':
                        group_3_list.append(full_row)
                    
                    serial += 1  # Increment serial for next student

        # 3. Sort the list so we can find the First and Last student easily
        # Sorting by the third column (Student ID) numerically
        group_3_list.sort(key=lambda x: int(x[2]))

        # 4. Display the results for the Lab Report
        print(f"Total students found for Group 3: {len(group_3_list)}")
        
        print("\nList of Students:")
        for student in group_3_list:
            print(f"Serial: {student[0]} | ID: {student[2]} | Name: {student[1]}")

        # Show the boundary students as requested by instructions
        if group_3_list:
            print(f"\nFirst Student in Group: {group_3_list[0][1]} (ID: {group_3_list[0][2]})")
            print(f"Last Student in Group: {group_3_list[-1][1]} (ID: {group_3_list[-1][2]})")

        # 5. Write the final collected list to the new file
        with open(output_file, mode='w', newline='') as out_file:
            writer = csv.writer(out_file)
            writer.writerows(group_3_list)

        print(f"\nFile '{output_file}' has been created successfully.")

    except FileNotFoundError:
        print("Error: Please make sure 'students.txt' is in the same folder.")

if __name__ == "__main__":
    main()