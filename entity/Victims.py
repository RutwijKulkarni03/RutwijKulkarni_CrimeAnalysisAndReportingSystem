class Victim:
    def __init__(self, victim_id, first_name, last_name, date_of_birth, gender, address, phone_number):
        self.__victim_id = victim_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__gender = gender
        self.__address = address
        self.__phone_number = phone_number


    def __str__(self):
        return f"Victim(ID: {self.__victim_id}, FirstName: {self.__first_name}, LastName: {self.__last_name}, DateOfBirth: {self.__date_of_birth}, Gender: {self.__gender}, Address: {self.__address}, PhoneNumber: {self.__phone_number})"
