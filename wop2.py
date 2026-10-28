class IOString():

    def _init_(self):
        self.srt1 = ""


    def get_String(self):
        self.str1 = input("enter the string : ")


    def print_String(self):
        print("result is :", self.str1.upper())


str1 = IOString()

str1.get_String()
str1.print_String()