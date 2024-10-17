import pyodbc
from entity.JobListing import JobListing
from entity.JobApplication import JobApplication
from dao.IVirtualJobBoard import IVirtualJobBoard
from util.DBConnUtil import DBConnUtil
from exception import DatabaseConnectionException

class JobBoardServiceImpl(IVirtualJobBoard):
    def __init__(self):
        self.connection = DBConnUtil.get_connection()

    def postJob(self, jobListing):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO JobListings (CompanyID, JobTitle, JobDescription, JobLocation, Salary, JobType, PostedDate) VALUES (?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (jobListing.get_companyID(), jobListing.get_jobTitle(), jobListing.get_jobDescription(), 
                                   jobListing.get_jobLocation(), jobListing.get_salary(), jobListing.get_jobType(), 
                                   jobListing.get_postedDate()))
            self.connection.commit()
        except Exception as e:
            raise DatabaseConnectionException("Error while posting job: " + str(e))

    def applyForJob(self, jobApplication):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO JobApplications (JobID, ApplicantID, ApplicationDate, CoverLetter) VALUES (?, ?, ?, ?)"
            cursor.execute(query, (jobApplication.get_jobID(), jobApplication.get_applicantID(), 
                                   jobApplication.get_applicationDate(), jobApplication.get_coverLetter()))
            self.connection.commit()
        except Exception as e:
            raise DatabaseConnectionException("Error while applying for job: " + str(e))

    def getJobListings(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM JobListings")
        return cursor.fetchall()

    def getApplicantsForJob(self, jobID):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Applicants WHERE ApplicantID IN (SELECT ApplicantID FROM JobApplications WHERE JobID = ?)", (jobID,))
        return cursor.fetchall()
