import csv
import spacy
from bloomlevel import Bloom_Level
from outcome import Outcome
from assessmenttask import Assessment_Task


nlp = spacy.load('en_core_web_trf')

filename = input("Enter the file name: ")
unit_learning_outcomes = []
bloom_levels = {}
assessment_tasks = []
bloom_warnings = []



def read_bloom_verbs(level, weight):
    bloom_levels[level] = Bloom_Level('blooms/'+level+'.txt', level, weight)



# Open CSV containing unit guide information

with open(filename, newline='') as unit_guide:
    unit_guide_reader = csv.DictReader(unit_guide)


    # Read all unique outcomes into list
    for row in unit_guide_reader:
        assessment_outcomes = str(row['Learning Outcomes']).split(';')

        # Read in assessment task information, and string representation of outcomes
        assessment_tasks.append(Assessment_Task(row['Assessment Task'], row['Weighting'], row['Hurdle'], row['Due Date'], assessment_outcomes))

        for outcome in assessment_outcomes:
            outcome = outcome.strip()
            # Only add unique outcomes not already in the list
            if outcome not in unit_learning_outcomes:
                unit_learning_outcomes.append(outcome)


# Open rubric for each assessment (should one exist)
for assessment in assessment_tasks:
    rubric_name = input("Enter the rubric for " + assessment.task_name + ": ")
    if rubric_name != "":
        with open(rubric_name, newline='') as rubric:
            rubric_reader = csv.DictReader(rubric)
            field_names = rubric_reader.fieldnames

            for row in rubric_reader:
                category = row['Category']
                details = row['Details']
                grading_scale = {}
                for grade in field_names[2:]:
                    grading_scale[grade] = row[grade]
                

        


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

# Repalce str represenation of outcomes in assessment task with class version
for assessment in assessment_tasks:
    assessment_outcome_index = 0
    while assessment_outcome_index < len(assessment.outcomes):
        for outcome in unit_learning_outcomes:
            if outcome.outcome_description == assessment.outcomes[assessment_outcome_index]:
                assessment.outcomes[assessment_outcome_index] = outcome
                break
        assessment_outcome_index += 1           


# Split each assessment task so that they only have one due date (some tasks are submitted multiple times)
assessment_len = len(assessment_tasks)
for i in range(assessment_len):
    assessment = assessment_tasks[0]
    for date in assessment.due_date:
        split_task = Assessment_Task(assessment.task_name, assessment.weighting, assessment.hurdle, date, assessment.outcomes)
        split_task.due_date = int(split_task.due_date[0])
        assessment_tasks.append(split_task)

    # Remove the original item after it's been split
    assessment_tasks.pop(0)

# Sort by due date
assessment_tasks.sort(key = lambda x: x.due_date)

# Sort by bloom weight
unit_learning_outcomes.sort(key = lambda x: x.bloom_weight)

# All assessments should preferably contain the lowest level of blooms taxonomy (remember), and work their way up, 
# adding higher level concepts as the semester goes. Bloom levels should be introduced in order of assessment due date
# i.e. an outcome in the create level should not appear, and be assessed before an outcome assessing the apply level has
# been checked (though they can appear on the same assessment)

# Check that each subsequent assessment is still assessing lower level skills

for outcome in unit_learning_outcomes:
    # Ignore assessments until the tested outcome first appears
    outcome_occurred = False
    for assessment in assessment_tasks:
        if outcome_occurred == False and outcome in assessment.outcomes:
            outcome_occurred = True
        
        
        if outcome_occurred:
            assessment_contains_level = False
            for assessment_outcome in assessment.outcomes:
                if outcome.bloom_weight == assessment_outcome.bloom_weight:
                    assessment_contains_level = True
                    break
            # Should an assessment not contain an outcome of the expected bloom level, a warning is created
            if not assessment_contains_level:
                warning = "Warning: Bloom level {bloom_level} does not appear in assessment {assessment}".format(bloom_level = outcome.bloom_level, assessment = assessment.task_name)
                if warning not in bloom_warnings:
                    bloom_warnings.append(warning)

# Check that higher level outcomes aren't tested before one of a lower level appears
# For example, an outcome assessing create should not appear before one assessing apply
# The already assessed weights


checked_outcomes = []
# Prefill list (may be better way to do this)
for outcome in assessment_tasks[0].outcomes:
    if outcome.bloom_weight not in checked_outcomes:
        checked_outcomes.append(outcome.bloom_weight)

for assessment in assessment_tasks:
    for outcome in assessment.outcomes:
        bloom_weight = outcome.bloom_weight
        for checked in checked_outcomes:
            # print("""
            #       Checked: {checked}
            #       bloom_weight: {bloom_weight}
            #       checked outcomes: {checked_outcomes}

            #     ----------------------------------------------------
            #       """.format(checked = checked, bloom_weight = bloom_weight, checked_outcomes = checked_outcomes))
            if bloom_weight < checked and bloom_weight not in checked_outcomes:
                #TODO append this to list rather than print
                print("Warning: Bloom level {higher_level} appears before Bloom level {lower_level} in assessment task {assessment}".format     
                      (higher_level = checked, lower_level = bloom_weight, assessment = assessment.task_name))


        if bloom_weight not in checked_outcomes:
            checked_outcomes.append(bloom_weight)
    
for warning in bloom_warnings:
    print(warning)

    

      

    
    




   
            









