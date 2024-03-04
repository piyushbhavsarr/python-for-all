class OperatorPrecedenceDemo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def demonstrate_math_operations(self):
        result = (self.x + self.y) * 2 ** 2 / 4
        print("Math Operations Result:", result)

    def demonstrate_bitwise_operations(self):
        result_and = self.x & self.y
        result_xor = self.x ^ self.y
        result_or = self.x | self.y
        print("Bitwise AND Result:", result_and)
        print("Bitwise XOR Result:", result_xor)
        print("Bitwise OR Result:", result_or)

    def demonstrate_logical_operations(self):
        result_not = not (self.x > self.y)
        result_and = (self.x > 0) and (self.y < 10)
        result_or = (self.x > 0) or (self.y < 10)
        print("Logical NOT Result:", result_not)
        print("Logical AND Result:", result_and)
        print("Logical OR Result:", result_or)

    def demonstrate_comparison_operations(self):
        result_eq = self.x == self.y
        result_gt = self.x > self.y
        result_in = self.x in range(10)
        print("Equality Result:", result_eq)
        print("Greater Than Result:", result_gt)
        print("Membership Test Result:", result_in)

    def run_demonstrations(self):
        print("Initial Values: x =", self.x, ", y =", self.y)
        print("=" * 40)

        self.demonstrate_math_operations()
        print("=" * 40)

        self.demonstrate_bitwise_operations()
        print("=" * 40)

        self.demonstrate_logical_operations()
        print("=" * 40)

        self.demonstrate_comparison_operations()


# Instantiate the OperatorPrecedenceDemo class
demo_instance = OperatorPrecedenceDemo(5, 3)

# Run the demonstrations
demo_instance.run_demonstrations()