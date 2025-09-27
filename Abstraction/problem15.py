# Q15. Cloud Storage (Google Drive vs Dropbox)
from abc import ABC, abstractmethod

class CloudStorage(ABC):
    @abstractmethod
    def upload(self, file):
        pass

class GoogleDrive(CloudStorage):
    def upload(self, file):
        return f"Uploaded {file} to Google Drive"

class Dropbox(CloudStorage):
    def upload(self, file):
        return f"Uploaded {file} to Dropbox"

c = GoogleDrive()
print(c.upload("Project.zip"))


# Q15. Cloud Storage (Google Drive vs Dropbox)
# Common kaam: file upload karna.
# Lekin backend service (API, server) alag hote hain.
# Abstraction: upload(file) sab jagah same hai.