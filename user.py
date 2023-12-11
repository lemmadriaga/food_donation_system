from person import Person

class User(Person):
    def __init__(self, username, password, first_name, last_name, phone_number):
        super().__init__(username, password, first_name, last_name, phone_number)
        self.donations = []
        self.points = 0
        self.badges = []

    def earn_points(self, points):
        self.points += points
