class FileUploadException(Exception):
    def __init__(self, message="Error during file upload. File not found or unsupported format."):
        self.message = message
        super().__init__(self.message)