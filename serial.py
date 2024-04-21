"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start = 0):
        """ Initialize generator. If start is not given, will set start at 0"""
        self.start = start
        self.count = 0

    def generate(self):
        """returns the next number in the serial"""
        self.count += 1
        return self.start + self.count - 1

        
    def reset(self):
        """Reset SerialGenerator's count back to 0"""
        self.count = 0

