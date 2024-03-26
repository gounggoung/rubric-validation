import csv

filename = input("Enter the file name: ")
unit_learning_outcomes = []

with open(filename, newline='') as unit_guide:
    unit_guide_reader = csv.DictReader(unit_guide, delimiter=';')
    for row in unit_guide_reader:
        assessment_outcomes = str(row['Learning Outcomes']).split(',')
        for outcome in assessment_outcomes:
            outcome = outcome.strip()
            if outcome not in unit_learning_outcomes:
                unit_learning_outcomes.append(outcome)

print(len(unit_learning_outcomes))






