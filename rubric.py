import csv

from rubricrow import RubricRow


class Rubric:

    

    def __init__(self, assessment):

        self.rows = []


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
                    self.rows.append(RubricRow(category, details, grading_scale))
    
    def __repr__(self):
        return (str(self.rows))
            
            