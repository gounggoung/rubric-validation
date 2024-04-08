class Outcome:


    # outcome_description: str
    # bloom_level: Bloom_Level
    # id: int
    def __init__(self, outcome_description, bloom_level, bloom_weight, id):
       self.outcome_description = outcome_description
       self.bloom_level = bloom_level
       self.bloom_weight = bloom_weight
       self.id = id 
    
    def __repr__(self):
        return "{id}    {bloom_level}: {outcome_description}".format(id=self.id, bloom_level=self.bloom_level, outcome_description=self.outcome_description)