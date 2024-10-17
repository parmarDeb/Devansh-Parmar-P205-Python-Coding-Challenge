import pyodbc

class DBPropertyUtil:
    @staticmethod
    def get_property_string():
        # Example values; replace these with your actual configuration retrieval logic
        host = r"DESKTOP-G4PDNF1\\SQLEXPRESS"  # e.g., "localhost" or "192.168.1.1"
        user = "DESKTOP-G4PDNF1\Hp"
        password = ""
        database = "CareerHub"
        port = "1433"         
        return host, user, password, database, port