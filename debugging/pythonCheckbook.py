class Checkbook:
    def __init__(self):
        # Initialize the balance to zero
        self.balance = 0.0

    def deposit(self, amount):
        # Add the deposited amount to the balance
        self.balance += amount
        # Print deposit confirmation and current balance
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        # Check if there are sufficient funds for the withdrawal
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            # Subtract the withdrawal amount from the balance
            self.balance -= amount
            # Print withdrawal confirmation and current balance
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        # Print the current balance
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    # Create a new instance of the Checkbook class
    cb = Checkbook()
    # Main loop for user interaction
    while True:
        # Prompt the user for action
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        # Check user input and perform corresponding action
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            amount = float(input("Enter the amount to deposit: $"))
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = float(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    # Call the main function to start the program
    main()

