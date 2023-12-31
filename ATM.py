class Atm:
    #constructor
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
    Hi How can I help you ?
    1. press 1 to create pin
    2. press 2 to change pin
    3. press 3 to  check balance
    4. press 4 to withdraw
    5. press 5 to Exit
    """ )
        

        if user_input == "1":
            #create pin
            self.create_pin()
        elif user_input == "2":
            #change pin
            self.change_pin()
        elif user_input == "3":
            #check balance
            self.check_bal()
        elif user_input == "4":
            self.withdraw()
            pass
        else:
            exit()

    def create_pin(self):
        user_pin = int(input("Enter your pin: "))
        self.pin = user_pin
        user_bal = int(input("Enter your balance: "))
        self.balance = user_bal
        self.menu()

        print("Pin created successfully")

    def change_pin(self):
        old_pin = int(input("Enter your current pin: "))

        if old_pin == self.pin:
            new_pin = int(input("Enter new pin: "))
            self.pin = new_pin
            print("Pin has been changes successfully")
            self.menu()
        else:
            print("Wrong pin")
            self.menu()

    def check_bal(self):
        user_pin = int(input("Enter your pin: "))
        if user_pin == self.pin:
            print("Balance: ", self.balance)
        else:
            print("Wrong pin")
    
    def withdraw(self):
        user_pin = int(input("Enter the Pin: "))
        if user_pin == self.pin:
            amount= int(input("Enter the amount: "))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print("Withdrawl successful ")
            else:
                print("insufficient balance")
        else:
            print("Wrong Pin")
        self.menu()




obj = Atm()