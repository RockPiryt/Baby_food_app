class Baby:

    def __init__(self,day, birth_weight):
        self.day = day 
        self.birth_weight = birth_weight
    
    def calc_current_weight(self):
        '''Method to calculate actual baby weight starting from birth weight.'''
        
        return self.birth_weight + (20 * self.day)