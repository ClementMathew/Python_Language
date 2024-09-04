

from savings_account import SavingsAccount

class RestrictedSavingsAccount(SavingsAccount):
    """This class represents a restricted savings account with a limit on the number of withdrawals."""

    MAX_WITHDRAWALS = 3  # Maximum number of allowed withdrawals per month

    def __init__(self, name, pin, balance=0.0):
        """Initializes the attributes of the RestrictedSavingsAccount, including a withdrawal counter."""
        # Call the superclass (SavingsAccount) constructor
        super().__init__(name, pin, balance)
        self.counter = 0  # Initialize the withdrawal counter

    def withdraw(self, amount):
        """Restricts the number of withdrawals to MAX_WITHDRAWALS."""
        if self.counter >= RestrictedSavingsAccount.MAX_WITHDRAWALS:
            return "No more withdrawals allowed this month"
        else:
            message = super().withdraw(amount)  # Call the withdraw method from SavingsAccount
            if message is None:  # If withdrawal is successful
                self.counter += 1  # Increment the withdrawal counter
            return message

    def resetCounter(self):
        """Resets the withdrawal counter, typically at the start of a new month."""
        self.counter = 0


# Create a restricted savings account
account = RestrictedSavingsAccount("Jane Doe", "5678", 2000)

# Try withdrawing money
print(account.withdraw(500))  # Successful withdrawal
print(account.withdraw(300))  # Successful withdrawal
print(account.withdraw(200))  # Successful withdrawal
print(account.withdraw(100))  # Should return "No more withdrawals allowed this month"

# Reset the counter for a new month
account.resetCounter()

# Withdraw again after reset
print(account.withdraw(100))  # Successful withdrawal

# Print account details
print(account)
