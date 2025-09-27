# Q4. Notification System (Email, SMS)

# Logic: Different notifications ka implementation.
from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        return f"Email sent: {message}"

class SMSNotification(Notification):
    def send(self, message):
        return f"SMS sent: {message}"

n = EmailNotification()
print(n.send("Hello User"))


# Q4. Notification System (Email, SMS)
# Notification bhejna hai (same function = send(message)).
# Backend me agar email hai to SMTP use hoga, SMS ke liye telecom API.
# User ko fark nahi padta, use sirf send() karna hai.
