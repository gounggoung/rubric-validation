class Bloom_Level:
    
    def __init__(self, verb_list, level_name, level_weight):
        with open(verb_list) as verbs:
            self.verb_list = verbs.readline().split(',')

        self.level_name = level_name
        self.weight = level_weight


    def __repr__(self):
        return str(self.level_name)
    