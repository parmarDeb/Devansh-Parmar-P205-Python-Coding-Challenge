class InvalidEmailFormatException(Exception):
    def __init__(self, message="Invalid email format. Please provide a valid email address."):
        self.message = message
        super().__init__(self.message)