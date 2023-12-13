from enum import Enum

class Gender(Enum):
    FEMALE = 1
    MALE = 2
    NON_BINARY = 3

class Guest:
    def __init__(self, guest_id, name, age, city, phone_number, gender):
        self.id = guest_id
        self.name = name
        self.age = age
        self.city = city
        self.phone_number = phone_number
        self.gender = gender

class Party:
    def __init__(self, day, reason, guests):
        self.day = day
        self.reason = reason
        self.guests = guests

    def find_average_age(self, gender):

        total_age = 0
        count = 0
        for guest in self.guests:
            if guest.gender == gender:
                total_age += guest.age
                count += 1
        if count == 0:
            return 0
        else:
            return total_age / count

    def is_lucky_phone_number(self, phone_number):
        return str(phone_number).count('7') >= 3


    def print_sorted_guests(self):
            sorted_guests = sorted(self.guests, key=lambda x: x.id)
            print("Сортовані гості за ID:")
            for guest in sorted_guests:
                print(f"ID: {guest.id}, Name: {guest.name}, Age: {guest.age}, Gender: {guest.gender}")

def main():
    guest1 = Guest(1, "Michael", 22, "Kyiv", "123456789", Gender.MALE)
    guest2 = Guest(2, "Aleka", 19, "Lviv", "777123456", Gender.FEMALE)
    guest3 = Guest(3, "Vladik", 22, "Odessa", "666777888", Gender.NON_BINARY)
    guest4 = Guest(4, "Bob", 20, "Lviv", "666777999", Gender.MALE)

    party = Party("2023-11-16", "Birthday Party", [guest1, guest2, guest3, guest4])

    average_age_male = party.find_average_age(Gender.MALE)
    print(f"Середній вік чоловіків на вечірці: {average_age_male}")

    lucky_phone_number = party.is_lucky_phone_number(guest2.phone_number)
    print(f"Чи номер щасливий? : {lucky_phone_number}")

    party.print_sorted_guests()

if __name__ == "__main__":
    main()
