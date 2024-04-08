class Assessment_Task:
    
    def __init__(self, task_name, weighting, hurdle, due_date, outcomes):
        self.task_name = task_name
        self.weighting = weighting
        
        if(hurdle == 'Yes'):
            self.hurdle = True
        else:
            self.hurdle = False

        
        self.due_date = due_date
        self.outcomes = outcomes

    def __repr__(self):
        return "{task_name}     {weighting}     {hurdle}    {due_date}".format(task_name = self.task_name, weighting = self.weighting, hurdle = self.hurdle, due_date = self.due_date)