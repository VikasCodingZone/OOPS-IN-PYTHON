#Q20. Private Method Restriction

class Phone:
    def __secret_feature(self):
        print("Secret Code Running")

    def access(self):
        self.__secret_feature()

p = Phone()
p.access()


# Logic: Private method ko sirf class ke andar call kar sakte hain