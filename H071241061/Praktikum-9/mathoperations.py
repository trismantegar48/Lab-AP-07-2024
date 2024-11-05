class MathOperations:

    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

    def digit_sum(self, n):
        return sum(int(digit) for digit in str(n))
    
# math_ops = MathOperations()
# print(math_ops.factorial(4))
# print(math_ops.digit_sum(12345))
