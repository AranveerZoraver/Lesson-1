class Employee:

    def _init_(self):
        print("Employee Created")


    def _del_(self):
        print("destructor called")


def Create_obj():
    print('making object')
    obj = Employee()
    print('function end...')
    return obj

print('Calling Create_obj() function...')
obj = Create_obj()
print('progra end...')