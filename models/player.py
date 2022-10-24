GENDER = ("male", "female", "")

class Player:
    def __init__(self, lastname, firstname, birthday, gender, rank):
        self.lastname = lastname
        self.firstname = firstname
        self.birthday = birthday
        self.gender = GENDER.index(gender)
        self.rank = rank
        self.score = 0
        self.opponent_list = []