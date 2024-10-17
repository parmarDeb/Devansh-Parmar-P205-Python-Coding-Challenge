class DatabaseConnectionException(Exception):
    def __init__(self, message="Database connection failed."):
        self.message = message
        super().__init__(self.message)