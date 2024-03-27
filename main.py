import csv
import spacy


nlp = spacy.load('en_core_web_trf')

filename = input("Enter the file name: ")
unit_learning_outcomes = []
bloom_levels = {}



def read_bloom_verbs(level):
    with open('blooms\\'+level+'.txt') as verbs:
        bloom_levels[level] = verbs.readline().split(',')



# Open CSV containing unit guide information
with open(filename, newline='') as unit_guide:
    unit_guide_reader = csv.DictReader(unit_guide)
    for row in unit_guide_reader:
        assessment_outcomes = str(row['Learning Outcomes']).split(';')
        for outcome in assessment_outcomes:
            outcome = outcome.strip()
            if outcome not in unit_learning_outcomes:
                unit_learning_outcomes.append(outcome)

# Read in bloom levels from text file
read_bloom_verbs('knowledge')
read_bloom_verbs('comprehend')
read_bloom_verbs('apply')
read_bloom_verbs('analyze')
read_bloom_verbs('synthesize')
read_bloom_verbs('evaluate')



for outcome in unit_learning_outcomes:
    for token in nlp(outcome):
        if token.pos_ == "VERB":
            for level in bloom_levels:
                if bloom_levels[level].count(token.text.lower()) > 0:
                    print(level + ': ' + outcome)
            break
                







