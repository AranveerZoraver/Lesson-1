class Account:
    def __init__(self, owner, pin):
        self.owner = owner
        self.__pin = pin

    def check_pin(self, guess):
        return guess == self.__pin

    def set_pin(self, new_pin):
        if isinstance(new_pin, str) and new_pin.isdigit() and len(new_pin) == 4:
            self.__pin = new_pin
            return True
        return False

    def __str__(self):
        return f"Account owner: {self.owner} | PIN: ****"


acct = Account("Aran", "1234")

try:
    print(acct.__pin)
except AttributeError as e:
    print("Direct access failed:", e)

print(acct.check_pin("1234"))
print(acct.set_pin("12"))
print(acct.set_pin("4321"))
print(acct.check_pin("4321"))
print(acct)