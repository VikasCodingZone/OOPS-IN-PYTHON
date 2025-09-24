# Q18. Polymorphism with file-like objects
class FileReader:
    def read(self):
        print("Reading file")

class NetworkReader:
    def read(self):
        print("Reading network stream")

for reader in [FileReader(), NetworkReader()]:
    reader.read()


#     Logic:

# Function kisi bhi “reader” type ke object ke liye kaam karta
# Explanation:

# Duck typing → polymorphic behavior