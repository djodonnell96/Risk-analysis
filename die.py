import random

class die:
    def __init__(self,v = None):

        if v == None:
            self.value = random.randint(1,6)
        else:
            self.value = v

    def getValue():
        return self.value

    def roll():
        self.value = random.randint(1,6)