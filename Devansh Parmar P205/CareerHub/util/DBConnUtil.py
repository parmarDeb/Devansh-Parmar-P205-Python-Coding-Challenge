import pyodbc

class DBConnUtil:
    @staticmethod
    def get_connection():
        try:
            # Fetching connection properties
            host, database = "DESKTOP-G4PDNF1\\SQLEXPRESS", "CareerHub"
            
            connection_string = (
                f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                f'SERVER={host};'
                f'DATABASE={database};'
                f'Trusted_Connection=yes;'
            )

            connection = pyodbc.connect(connection_string)
            return connection
        except pyodbc.Error as e:
            print(f"Failed to connect to the database: {e.args}")
            raise