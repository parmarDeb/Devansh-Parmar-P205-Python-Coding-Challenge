from abc import ABC, abstractmethod

class IVirtualJobBoard(ABC):
    @abstractmethod
    def postJob(self, jobListing):
        pass

    @abstractmethod
    def applyForJob(self, jobApplication):
        pass

    @abstractmethod
    def getJobListings(self):
        pass

    @abstractmethod
    def getApplicantsForJob(self, jobID):
        pass
