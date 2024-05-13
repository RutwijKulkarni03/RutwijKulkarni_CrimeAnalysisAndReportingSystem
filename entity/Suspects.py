class Suspect:
    def __init__(self, suspect_id, first_name, last_name, date_of_birth, gender, contact_info):
        self.__suspect_id = suspect_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__gender = gender
        self.__contact_info = contact_info


    def __str__(self):
        return f"Suspect(ID: {self.__suspect_id}, FirstName: {self.__first_name}, LastName {self.__last_name}, DateOfBirth: {self.__date_of_birth} Gender: {self.__gender}, ContactInformation: {self.__contact_info})"
