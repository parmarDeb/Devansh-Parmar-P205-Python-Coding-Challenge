import pyodbc
from util.DBConnUtil import DBConnUtil

class DatabaseManager:
    def __init__(self):
        # Get database connection
        self.connection = DBConnUtil.get_connection()
        self.cursor = self.connection.cursor()

    # Initialize the database (this could include table creation if necessary)
    def initialize_database(self):
        try:
            create_tables_query = """
            CREATE TABLE IF NOT EXISTS Company (
                CompanyID INT PRIMARY KEY IDENTITY(1,1),
                CompanyName VARCHAR(255),
                Location VARCHAR(255)
            );

            CREATE TABLE IF NOT EXISTS JobListing (
                JobID INT PRIMARY KEY IDENTITY(1,1),
                CompanyID INT,
                JobTitle VARCHAR(255),
                JobDescription TEXT,
                JobLocation VARCHAR(255),
                Salary DECIMAL(10, 2),
                JobType VARCHAR(50),
                PostedDate DATE,
                FOREIGN KEY (CompanyID) REFERENCES Company(CompanyID)
            );

            CREATE TABLE IF NOT EXISTS Applicant (
                ApplicantID INT PRIMARY KEY IDENTITY(1,1),
                FirstName VARCHAR(255),
                LastName VARCHAR(255),
                Email VARCHAR(255),
                Phone VARCHAR(50),
                Resume VARCHAR(255)
            );

            CREATE TABLE IF NOT EXISTS JobApplication (
                ApplicationID INT PRIMARY KEY IDENTITY(1,1),
                JobID INT,
                ApplicantID INT,
                ApplicationDate DATE,
                CoverLetter TEXT,
                FOREIGN KEY (JobID) REFERENCES JobListing(JobID),
                FOREIGN KEY (ApplicantID) REFERENCES Applicant(ApplicantID)
            );
            """
            self.cursor.execute(create_tables_query)
            self.connection.commit()
            print("Database initialized and tables created successfully.")
        except Exception as e:
            print(f"Error initializing database: {e}")

    # Insert a new job listing
    def insert_job_listing(self, job_title, job_description, job_location, salary, job_type, company_id):
        try:
            query = """
            INSERT INTO JobListing (CompanyID, JobTitle, JobDescription, JobLocation, Salary, JobType, PostedDate)
            VALUES (?, ?, ?, ?, ?, ?, GETDATE())
            """
            self.cursor.execute(query, (company_id, job_title, job_description, job_location, salary, job_type))
            self.connection.commit()
            print("Job listing inserted successfully.")
        except Exception as e:
            print(f"Error inserting job listing: {e}")

    # Insert a new company
    def insert_company(self, company_name, location):
        try:
            query = "INSERT INTO Company (CompanyName, Location) VALUES (?, ?)"
            self.cursor.execute(query, (company_name, location))
            self.connection.commit()
            print("Company inserted successfully.")
        except Exception as e:
            print(f"Error inserting company: {e}")

    # Insert a new applicant
    def insert_applicant(self, first_name, last_name, email, phone, resume):
        try:
            query = "INSERT INTO Applicant (FirstName, LastName, Email, Phone, Resume) VALUES (?, ?, ?, ?, ?)"
            self.cursor.execute(query, (first_name, last_name, email, phone, resume))
            self.connection.commit()
            print("Applicant inserted successfully.")
        except Exception as e:
            print(f"Error inserting applicant: {e}")

    # Insert a new job application
    def insert_job_application(self, job_id, applicant_id, cover_letter):
        try:
            query = """
            INSERT INTO JobApplication (JobID, ApplicantID, ApplicationDate, CoverLetter)
            VALUES (?, ?, GETDATE(), ?)
            """
            self.cursor.execute(query, (job_id, applicant_id, cover_letter))
            self.connection.commit()
            print("Job application inserted successfully.")
        except Exception as e:
            print(f"Error inserting job application: {e}")

    # Retrieve all job listings
    def get_job_listings(self):
        try:
            self.cursor.execute("SELECT * FROM JobListing")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error retrieving job listings: {e}")
            return []

    # Retrieve all companies
    def get_companies(self):
        try:
            self.cursor.execute("SELECT * FROM Company")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error retrieving companies: {e}")
            return []

    # Retrieve all applicants
    def get_applicants(self):
        try:
            self.cursor.execute("SELECT * FROM Applicant")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error retrieving applicants: {e}")
            return []

    # Retrieve applications for a specific job
    def get_applications_for_job(self, job_id):
        try:
            self.cursor.execute("SELECT * FROM JobApplication WHERE JobID = ?", (job_id,))
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error retrieving applications: {e}")
            return []

    # Close the database connection
    def close(self):
        self.connection.close()

if __name__ == '__main__':
    db_manager = DatabaseManager()
    db_manager.initialize_database()