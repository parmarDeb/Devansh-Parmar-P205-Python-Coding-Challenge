class JobListing:
    def __init__(self, jobID=None, companyID=None, jobTitle=None, jobDescription=None, jobLocation=None, salary=None, jobType=None, postedDate=None):
        self.__jobID = jobID
        self.__companyID = companyID
        self.__jobTitle = jobTitle
        self.__jobDescription = jobDescription
        self.__jobLocation = jobLocation
        self.__salary = salary
        self.__jobType = jobType
        self.__postedDate = postedDate