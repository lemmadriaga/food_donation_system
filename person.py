import hashlib

class Person:
    def __init__(self, username, password, first_name, last_name, phone_number):
        self.username = username
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
