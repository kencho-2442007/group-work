# Lab03_3.py
# Purpose: Filter students whose IDs end with 6 or 7

output_filename = "group_3.txt" 

try:
    with open("student.txt", "r") as student_file:
        lines = student_file.readlines()
except FileNotFoundError:
    print("Error: 'student.txt' not found.")
    exit()

if not lines:
    print("Error: The file is empty.")
    exit()

#Step 1: Parse Header
#Use the names from the provided data: SL.No., Name, Std. Id
columns = [c.strip() for c in lines[0].strip().split('\t')]
#If your file uses commas instead of tabs, change .split('\t') to .split(',')

data_lines = lines[1:]

all_students = []
for line in data_lines:
    line = line.strip()
    if not line:
        continue
    #Splitting by tab as per your sample data layout
    values = [v.strip() for v in line.split('\t') if v.strip()]
    
    if len(values) >= 3:
        student = {
            'SL.No': values[0],
            'Name': values[1],
            'ID': values[2]
        }
        all_students.append(student)

#Step 2: and now filter by ID ending in 6 or 7 
group_3_students = [s for s in all_students if s['ID'].endswith('6') or s['ID'].endswith('7')]

#Step 3: Sort by ID 
group_3_sorted = sorted(group_3_students, key=lambda s: s['ID'])

#Step 4: Identify First and Last 
if group_3_sorted:
    first_student = group_3_sorted[0]
    last_student = group_3_sorted[-1]
else:
    print("No students found ending in 6 or 7.")
    exit()

#Step 5: Display and Save Results 
output_lines = []

def add_line(text):
    print(text)
    output_lines.append(text)

add_line("=" * 50)
add_line("       STUDENTS WITH IDs ENDING IN 6 OR 7")
add_line("=" * 50)
add_line(f"\nTotal number of students found: {len(group_3_sorted)}\n")

add_line("Names of selected students:")
add_line("-" * 30)
for idx, student in enumerate(group_3_sorted, start=1):
    add_line(f"  {idx}. {student['Name']} (ID: {student['ID']})")

add_line("\n" + "-" * 50)
add_line("First Student (by ID):")
add_line(f"  ID   : {first_student['ID']}")
add_line(f"  Name : {first_student['Name']}")

add_line("\nLast Student (by ID):")
add_line(f"  ID   : {last_student['ID']}")
add_line(f"  Name : {last_student['Name']}")
add_line("=" * 50)

with open(output_filename, "w") as out_file:
    out_file.write("\n".join(output_lines))

print(f"\nSuccess! Results saved to '{output_filename}'.")