from fractions import Fraction
class Solution:
    def fractionAddition(self, expression: str) -> str:
        result = Fraction(0, 1)
        i = 0
        while i < len(expression):

            start = i
            if expression[i] in '+-':  # Skip over the sign
                i += 1
            while i < len(expression) and expression[i] not in '+-':
                i += 1
            

            fraction = Fraction(expression[start:i])
            result += fraction
        
        
        return f"{result.numerator}/{result.denominator}"