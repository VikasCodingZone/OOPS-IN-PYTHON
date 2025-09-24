# Q17. Using polymorphism in GUI buttons (example)
class Button:
    def click(self):
        print("Button clicked")

class ImageButton(Button):
    def click(self):
        print("Image Button clicked")

for btn in [Button(), ImageButton()]:
    btn.click()


    
# Logic:

# Same interface (click()) multiple button types ke liye
# Explanation:

# Runtime decide hota kaunsa method call hoga → dynamic polymorphism