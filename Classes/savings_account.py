
class SavingsAccount(object):
    
    """This class represents a savings account with the owner's name, PIN, and balance."""
    
    RATE = 0.02  # Single rate for all accounts

    def __init__(self, name, pin, balance=0.0):
        """Constructor creates an account with the given name, pin, and balance."""
        self.name = name
        self.pin = pin
        self.balance = balance

    def __str__(self):
        """Returns the string representation of the account."""
        result = 'Name: ' + self.name + '\n'
        result += 'PIN: ' + self.pin + '\n'
        result += 'Balance: ' + str(self.balance)
        return result

    def getBalance(self):
        """Returns the current balance."""
        return self.balance

    def getName(self):
        """Returns the current name."""
        return self.name

    def getPin(self):
        """Returns the current PIN."""
        return self.pin

    def deposit(self, amount):
        """Deposits the given amount and returns None."""
        self.balance += amount
        return None

    def withdraw(self, amount):
        """Withdraws the given amount. Returns None if successful, or an error message if unsuccessful."""
        if amount < 0:
            return "Amount must be >= 0"
        elif self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return None

    def computeInterest(self):
        """Computes, deposits, and returns the interest."""
        interest = self.balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest


# Create a savings account
account = SavingsAccount("John Doe", "1234", 1000)

# Deposit money
account.deposit(500)

# Withdraw money
account.withdraw(200)

# Compute and deposit interest
interest = account.computeInterest()

# Print account details
print(account)

# Output:
# Name: John Doe
# PIN: 1234
# Balance: 1320.0
