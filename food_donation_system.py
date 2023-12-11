import hashlib
from user import User 
from shelter import Shelter

class DonationSystem:
    def __init__(self):
        self.users = []
        self.shelters = []
        self.recent_donations = []

    def register_user(self):
        print("Register:")
        username = input("Enter username: ")
        password = input("Enter password: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone_number = input("Enter phone number: ")

        user = User(username, password, first_name, last_name, phone_number)
        self.users.append(user)
        print("Registration successful!")

    def login_user(self):
        print("Login:")
        username = input("Enter username: ")
        password = input("Enter password: ")

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        user = next((u for u in self.users if u.username == username and u.password == hashed_password), None)
        if user:
            print(f"Welcome, {user.first_name}!")
            self.user_menu(user)
        else:
            print("Invalid username or password. Please try again.")

    def user_menu(self, user):
        while True:
            print("\nOptions:")
            print("1. Donate")
            print("2. Register a Shelter")
            print("3. Review/Recent Donations")
            print("4. Cancel/Delete Donation")
            print("5. Logout")

            choice = input("Enter your choice (1/2/3/4/5): ")

            if choice == '1':
                self.donate_menu(user)
            elif choice == '2':
                self.register_shelter()
            elif choice == '3':
                self.review_donations()
            elif choice == '4':
                self.cancel_donation(user)
            elif choice == '5':
                print("Logged out.")
                break
            else:
                print("Invalid choice. Please try again.")

    def donate_menu(self, user):
        print("\nDonation Options:")
        print("1. Money")
        print("2. Food")
        print("3. Clothes")

        donation_type = input("Choose donation type (1/2/3): ")

        if donation_type == '1':
            amount = input("Enter the amount of money to donate: ")
            self.process_donation(user, f"Money Donation: ${amount}")
        elif donation_type == '2':
            food_type = input("Enter the type of food to donate: ")
            self.process_donation(user, f"Food Donation: {food_type}")
        elif donation_type == '3':
            clothes_type = input("Enter the type of clothes to donate: ")
            self.process_donation(user, f"Clothes Donation: {clothes_type}")
        else:
            print("Invalid choice. Please try again.")

    def process_donation(self, user, donation_description):
        print("\nAvailable Shelters:")
        for i, shelter in enumerate(self.shelters, start=1):
            print(f"{i}. {shelter.name} - {shelter.location} - {shelter.description}")

        shelter_choice = input("Choose a shelter (enter number): ")

        try:
            shelter_choice = int(shelter_choice)
            if 1 <= shelter_choice <= len(self.shelters):
                selected_shelter = self.shelters[shelter_choice - 1]
                print(f"\nThank you, {user.first_name}! You have donated to {selected_shelter.name}.")
                self.recent_donations.append({"user": user.first_name, "donation": donation_description, "shelter": selected_shelter.name})
                user.donations.append({"donation": donation_description, "shelter": selected_shelter.name})
            else:
                print("Invalid shelter choice. Donation canceled.")
        except ValueError:
            print("Invalid input. Donation canceled.")

    def register_shelter(self):
        print("\nRegister a Shelter:")
        shelter_type = input("Enter the type of shelter: ")
        name = input("Enter shelter name: ")
        location = input("Enter shelter location: ")
        description = input("Enter shelter description: ")

        shelter = Shelter(shelter_type, name, location, description)
        self.shelters.append(shelter)
        print("Shelter registration successful!")

    def review_donations(self):
        print("\nRecent Donations:")
        total_money_donations = 0
        for i, donation in enumerate(self.recent_donations, start=1):
            print(f"{i}. {donation['user']} donated {donation['donation']} to {donation['shelter']}")
            if "Money Donation" in donation['donation']:
                total_money_donations += float(donation['donation'].split("$")[1])

        print(f"\nTotal Money Donations: ${total_money_donations:.2f}")

    def cancel_donation(self, user):
        print("\nCancel/Delete Donation:")
        if not user.donations:
            print("You have no recent donations to cancel.")
            return

        print("Your Recent Donations:")
        for i, donation in enumerate(user.donations, start=1):
            print(f"{i}. {donation['donation']} to {donation['shelter']}")

        donation_choice = input("Choose a donation to cancel (enter number): ")

        try:
            donation_choice = int(donation_choice)
            if 1 <= donation_choice <= len(user.donations):
                canceled_donation = user.donations.pop(donation_choice - 1)
                self.recent_donations = [d for d in self.recent_donations if d != canceled_donation]
                print(f"\n{canceled_donation['donation']} to {canceled_donation['shelter']} has been canceled.")
            else:
                print("Invalid donation choice. Cancellation canceled.")
        except ValueError:
            print("Invalid input. Cancellation canceled.")

# Main program
donation_system = DonationSystem()

while True:
    print("\nMain Menu:")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    main_choice = input("Enter your choice (1/2/3): ")

    if main_choice == '1':
        donation_system.register_user()
    elif main_choice == '2':
        donation_system.login_user()
    elif main_choice == '3':
        print("Exiting the donation system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
