import sys
sys.path.append('F:\Python\Projects\Hexaware\CareerHub')
import pyodbc
from dao.JobBoardServiceImpl import JobBoardServiceImpl
from entity.JobListing import JobListing
from entity.Applicant import Applicant
from entity.JobApplication import JobApplication
from datetime import datetime

def menu():
    jobBoardService = JobBoardServiceImpl()

    while True:
        print("Menu:")
        print("1. Post Job")
        print("2. Apply for Job")
        print("3. Get Job Listings")
        print("4. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            # Job Posting
            jobTitle = input("Enter Job Title: ")
            jobDescription = input("Enter Job Description: ")
            jobLocation = input("Enter Job Location: ")
            salary = float(input("Enter Salary: "))
            jobType = input("Enter Job Type: ")
            postedDate = datetime.now()
            job = JobListing(None, 1, jobTitle, jobDescription, jobLocation, salary, jobType, postedDate)
            jobBoardService.postJob(job)
            print("Job Posted Successfully.")

        elif choice == 2:
            # Job Application
            jobID = int(input("Enter Job ID: "))
            applicantID = int(input("Enter Applicant ID: "))
            coverLetter = input("Enter Cover Letter: ")
            application = JobApplication(None, jobID, applicantID, datetime.now(), coverLetter)
            jobBoardService.applyForJob(application)
            print("Applied Successfully.")

        elif choice == 3:
            # Get Job Listings
            jobs = jobBoardService.getJobListings()
            for job in jobs:
                print(f"Job Title: {job[2]}, Salary: {job[5]}")

        elif choice == 4:
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    menu()