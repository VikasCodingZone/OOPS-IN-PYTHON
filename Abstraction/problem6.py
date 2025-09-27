# Q6. Database Connection (MySQL, MongoDB)

from abc import ABC, abstractmethod
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQL(Database):
    def connect(self):
        return "Connected to MySQL"

class MongoDB(Database):
    def connect(self):
        return "Connected to MongoDB"

db = MongoDB()
print(db.connect())


# Q6. Database Connection (MySQL, MongoDB)
# Common kaam: database se connect karna.
# Lekin connection process MySQL aur MongoDB me alag hota hai.
# User ko sirf connect() method dikhai deta hai.