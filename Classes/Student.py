class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """
        Constructor creates a Student with the given name and number of scores, and sets all scores to 0.
        """
        self.name = name
        self.scores = [0] * number  # Initialize all scores to 0

    def getName(self):
        """Returns the student's name."""
        return self.name

    def setScore(self, i, score):
        """
        Sets the ith score, counting from 1.
        """
        if 1 <= i <= len(self.scores):
            self.scores[i - 1] = score
        else:
            raise IndexError("Score index out of range")

    def getScore(self, i):
        """
        Returns the ith score, counting from 1.
        """
        if 1 <= i <= len(self.scores):
            return self.scores[i - 1]
        else:
            raise IndexError("Score index out of range")

    def getAverage(self):
        """Returns the average score."""
        if self.scores:  # Check if scores list is not empty
            return sum(self.scores) / len(self.scores)
        else:
            return 0

    def getHighScore(self):
        """Returns the highest score."""
        if self.scores:  # Check if scores list is not empty
            return max(self.scores)
        else:
            return 0

    def __str__(self):
        """Returns the string representation of the student."""
        return f"Name: {self.name}\nScores: {' '.join(map(str, self.scores))}"


s = Student("Clement", 3)

print(s)
print(s.getName())

s.setScore(1, 50)
s.setScore(2, 20)
s.setScore(3, 30)

print(s.getScore(1))
print(s.getScore(2))
print(s.getScore(3))

print(s.getAverage())
print(s.getHighScore())
