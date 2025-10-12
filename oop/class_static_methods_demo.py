class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        Does not depend on the class or instance.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        Has access to the class via 'cls' and can use class attributes.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b