class ApplicationDeadlineException(Exception):
    def __init__(self, message="Application deadline has passed. Cannot submit the application."):
        self.message = message
        super().__init__(self.message)
