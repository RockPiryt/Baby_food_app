
class ModifiedMilk:

    def __init__(self, user_portion, user_feeding):
        self.portion = user_portion
        self.feeding = user_feeding

    def calc_total_milk(self):
        '''Method to calculate total amount of milk for one day.'''
        return self.portion * self.feeding