class RubricRow:

    def __init__(self, category, details, grading_scale):
        self.category = category
        self.details = details
        self.grading_scale = grading_scale
    
    def __repr__(self):
        return """
                {category}
              
                {details}
              
                {grading_scale}
              
              """.format(category = self.category, details = self.details, grading_scale = self.grading_scale)
