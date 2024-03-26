import csv

filename = input("Enter the file name: ")

with open(filename) as rubric:
    lines = []
    for line in rubric:
        lines.append(line)



