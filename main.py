import csv
import spacy


nlp = spacy.load('en_core_web_trf')

filename = input("Enter the file name: ")
unit_learning_outcomes = []



# Open CSV containing unit guide information
with open(filename, newline='') as unit_guide:
    unit_guide_reader = csv.DictReader(unit_guide)
    for row in unit_guide_reader:
        assessment_outcomes = str(row['Learning Outcomes']).split(';')
        for outcome in assessment_outcomes:
            outcome = outcome.strip()
            if outcome not in unit_learning_outcomes:
                unit_learning_outcomes.append(outcome)



for outcome in unit_learning_outcomes:
    for token in nlp(outcome):
        if token.pos_ == "VERB":
            print(token.text)
            break
                







