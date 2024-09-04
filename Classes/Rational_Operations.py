class Rational:
    """Represents a rational number."""

    def __init__(self, numer, denom):
        """Constructor creates a number with the given numerator and denominator and reduces it to lowest terms."""
        self.numer = numer
        self.denom = denom
        self._reduce()

    def numerator(self):
        """Returns the numerator."""
        return self.numer

    def denominator(self):
        """Returns the denominator."""
        return self.denom

    def __str__(self):
        """Returns the string representation of the number."""
        return str(self.numer) + "/" + str(self.denom)

    def _reduce(self):
        """Helper to reduce the number to lowest terms."""
        divisor = self._gcd(self.numer, self.denom)
        self.numer = self.numer // divisor
        self.denom = self.denom // divisor

    def _gcd(self, a, b):
        """Euclid's algorithm for greatest common divisor (GCD)."""
        (a, b) = (max(a, b), min(a, b))
        while b > 0:
            (a, b) = (b, a % b)
        return a

    def __add__(self, other):
        """Returns the sum of the numbers.
        self is the left operand and other is the right operand."""
        newNumer = self.numer * other.denom + other.numer * self.denom
        newDenom = self.denom * other.denom
        return Rational(newNumer, newDenom)

    def __lt__(self, other):
        """Compares two rational numbers, self and other, using <."""
        extremes = self.numer * other.denom
        means = other.numer * self.denom
        return extremes < means

    def __eq__(self, other):
        """Tests self and other for equality."""
        if self is other:  # Object identity?
            return True
        elif type(self) != type(other):  # Types match?
            return False
        else:
            return self.numer * other.denom == other.numer * self.denom


# Create two Rational numbers
r1 = Rational(3, 4)  # Represents the rational number 3/4
r2 = Rational(2, 3)  # Represents the rational number 2/3

# Using the numerator() and denominator() methods
print("Numerator of r1:", r1.numerator())  # Output: 3
print("Denominator of r1:", r1.denominator())  # Output: 4

# Using the __str__() method (implicitly when printing)
print("r1 as a string:", r1)  # Output: 3/4
print("r2 as a string:", r2)  # Output: 2/3

# Using the __add__() method to add two rational numbers
r3 = r1 + r2  # 3/4 + 2/3
print("r1 + r2 =", r3)  # Output: 17/12

# Using the __lt__() method to compare two rational numbers
print("Is r1 less than r2?", r1 < r2)  # Output: False

# Using the __eq__() method to check if two rational numbers are equal
print("Is r1 equal to r2?", r1 == r2)  # Output: False

# Creating another rational number to test equality
r4 = Rational(6, 8)  # Represents the rational number 6/8 which reduces to 3/4
print("Is r1 equal to r4?", r1 == r4)  # Output: True