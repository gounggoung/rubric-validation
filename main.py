import csv
import spacy
from bloomlevel import Bloom_Level
from outcome import Outcome


nlp = spacy.load('en_core_web_trf')

filename = input("Enter the file name: ")
unit_learning_outcomes = []
bloom_levels = {}



def read_bloom_verbs(level, weight):
    bloom_levels[level] = Bloom_Level('blooms/'+level+'.txt', level, weight)



# Open CSV containing unit guide information
# Read all unique outcomes into list
with open(filename, newline='') as unit_guide:
    unit_guide_reader = csv.DictReader(unit_guide)
    for row in unit_guide_reader:
        assessment_outcomes = str(row['Learning Outcomes']).split(';')
        for outcome in assessment_outcomes:
            outcome = outcome.strip()
            # Only add unique outcomes not already in the list
            if outcome not in unit_learning_outcomes:
                unit_learning_outcomes.append(outcome)



# Create bloom levels with their respective weights (higher weight indicates a higher level skill)
read_bloom_verbs('remember', 1)
read_bloom_verbs('understand', 2)
read_bloom_verbs('apply', 3)
read_bloom_verbs('analyze', 4)
read_bloom_verbs('evaluate', 5)
read_bloom_verbs('create', 6)
   


# Replace str outcomes with class representation
outcome_index = 0
while outcome_index < len(unit_learning_outcomes):
    outcome = unit_learning_outcomes[outcome_index]
    for token in nlp(outcome):
        if token.pos_ == "VERB":
            for level in bloom_levels:
                if bloom_levels[level].verb_list.count(token.text.lower()) > 0:
                    unit_learning_outcomes[outcome_index] = Outcome(outcome, bloom_levels[level], bloom_levels[level].weight, outcome_index)
                    break
    outcome_index += 1
                

for outcome in unit_learning_outcomes:
    print(outcome)





