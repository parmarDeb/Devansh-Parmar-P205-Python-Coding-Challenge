class Applicant:
    def __init__(self, applicantID=None, firstName=None, lastName=None, email=None, phone=None, resume=None):
        self.__applicantID = applicantID
        self.__firstName = firstName
        self.__lastName = lastName
        self.__email = email
        self.__phone = phone
        self.__resume = resume