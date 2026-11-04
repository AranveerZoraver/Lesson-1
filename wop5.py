class MyClass:

    __PrivateVar = 27;


    def __PrivMeth(self):
        print("im in my class")


    def hello(self):
        print("private variable value:  ",MyClass.__PrivateVar)

foo = MyClass()
foo.hello()
foo.__PrivMeth