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

    