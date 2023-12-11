from person import Person

class Shelter(Person):
    def __init__(self, shelter_type, name, location, description):
        super().__init__(username="", password="", first_name="", last_name="", phone_number="")
        self.shelter_type = shelter_type
        self.name = name
        self.location = location
        self.description = description
