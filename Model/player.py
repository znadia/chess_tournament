import json

class Player:

    def __init__(self, name, first_name, d_o_b, sex):    
        self.name = name
        self.first_name = first_name
        self.d_o_b = d_o_b
        self.sex = sex
        self.score = 0
        self.ranking = 0

    # def __str__(self):
    #    return f"{self.name}, {self.first_name}, {self.d_o_b}, {self.sex}, {self.score}"

    def __repr__(self):
        return f"namesssss: {self.name}, first_name: {self.first_name}, d_o_b: {self.d_o_b}, sex: {self.sex}, score: {self.score}, classement: {self.ranking}"
        #return self.name
