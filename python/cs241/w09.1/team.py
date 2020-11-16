class BalanceError(Exception):
    def __init__(self,message):
        super().__init__(message)
    
class OutOfChecksError(Exception):
    def __init__(self,message):
        super().__init__(message)
    

class CheckingAccount:
    def __init__(self,starting_balance, num_checks):
        self.balance=starting_balance
        self.check_count=num_checks
        
    def deposit(self, amount):
        self.balance += amount
    
    def write_check(self, amount):
        if self.balance <= 0 or amount > self.balance:
            raise BalanceError("Your balance is lower than required")
        if self.check_count <= 0:
            raise OutOfChecksError("You're out of checks")            

        self.balance -= amount
        self.check_count -= 1       
    def display(self):
        print("Your current balance is: ${:.2f}\nThe amount of checks is: {}".format(self.balance,self.check_count))
        
    def apply_for_credit(self,amount):
        pass

def display_menu():
    """
    Displays the available commands.
    """
    print()
    print("Commands:")
    print("  quit - Quit")
    print("  new - Create new account")
    print("  display - Display account information")
    print("  deposit - Desposit money")
    print("  check - Write a check")

def new_checks_menu():
    print()
    print("1. yes")
    print("2. no")

def main():
    """
    Used to test the CheckingAccount class.
    """
    acc = None
    command = ""

    while command != "quit":
        display_menu()
        command = input("Enter a command: ")

        if command == "new":
            balance = float(input("Starting balance: "))
            num_checks = int(input("Numbers of checks: "))

            acc = CheckingAccount(balance, num_checks)
        elif command == "display":
            acc.display()
        elif command == "deposit":
            amount = float(input("Amount: "))
            acc.deposit(amount)
        elif command == "check":
            amount = float(input("Amount: "))
            try:
                acc.write_check(amount)
            except BalanceError as e:
                print("Got an error: ", e)
            except OutOfChecksError as e:
                print("Got an error: ", e)                
                answer = int(input("Would you like you to buy more checks?\nYou will receive 25 checks and will be deducted $5.00 from your balance\n1. Yes\n2. No\n"))
                
                if answer == 1:
                    acc.check_count += 25
                    acc.balance -= 5
                else:
                    pass
            
        elif command == "credit":
            amount = float(input("Amount: "))
            acc.apply_for_credit(amount)

if __name__ == "__main__":
    main()

        