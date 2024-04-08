class Bloom_Level:
    
    def __init__(self, verb_list, level_weight):
        with open(verb_list) as verbs:
            self.verb_list = verbs.readline().split(',')
            
        self.weight = level_weight


    def __repr__(self):
        return str(self.verb_list)
    