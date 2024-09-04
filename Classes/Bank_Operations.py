
from savings_account import SavingsAccount

class Bank(object):

    """This class represents a bank that manages multiple savings accounts."""

    def __init__(self):
        """Initializes an empty bank with a dictionary to hold accounts."""
        self.accounts = {}

    def __str__(self):
        """Returns the string representation of the entire bank."""
        return '\n'.join(map(str, self.accounts.values()))

    def makeKey(self, name, pin):
        """Creates and returns a unique key from the name and pin."""
        return name + "/" + pin

    def add(self, account):
        """Inserts an account into the bank using name and pin as the key."""
        key = self.makeKey(account.getName(), account.getPin())
        self.accounts[key] = account

    def remove(self, name, pin):
        """Removes and returns an account with the given name and pin as the key."""
        key = self.makeKey(name, pin)
        return self.accounts.pop(key, None)

    def get(self, name, pin):
        """Returns an account with the given name and pin as the key, or None if not found."""
        key = self.makeKey(name, pin)
        return self.accounts.get(key, None)

    def computeInterest(self):
        """Computes and returns the total interest for all accounts."""
        total = 0.0
        for account in self.accounts.values():
            total += account.computeInterest()
        return total


# Create a bank
my_bank = Bank()

# Create some savings accounts
account1 = SavingsAccount("John Doe", "1234", 1000)
account2 = SavingsAccount("Jane Doe", "5678", 2000)

# Add accounts to the bank
my_bank.add(account1)
my_bank.add(account2)

# Print the bank's accounts
print("------- my_bank after adding accounts --------")
print(my_bank)

# Remove an account
my_bank.remove("John Doe", "1234")

# Print the bank's accounts after removal
print("------- my_bank after removed --------")
print(my_bank)

# Compute total interest for all accounts
total_interest = my_bank.computeInterest()
print(f"Total Interest: {total_interest}")
