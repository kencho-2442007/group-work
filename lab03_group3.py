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

