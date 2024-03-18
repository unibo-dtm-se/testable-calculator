import math

Number = int | float

MATH_FUNCTIONS = {
    "sqrt": math.sqrt,
}

class Calculator:

    def __init__(self):
        self.expression = ""

    def _ensure_is_digit(self, value: int | str):
        if isinstance(value, str):
            value = int(value)
        if value not in range(10):
            raise ValueError("Value must a digit in [0, 9]: " + value)
        return value

    def _append(self, value):
        self.expression += str(value)
    
    def digit(self, value: int | str):
        value = self._ensure_is_digit(value)
        self._append(value)
    
    def plus(self):
        self._append("+")

    def minus(self):
        self._append("-")
    
    def multiply(self):
        self._append("*")
    
    def divide(self):
        self._append("/")

    def dot(self):
        self._append(".")

    def clear(self):
        self.expression = ""

    def open_parenthesis(self):
        self._append("(")
    
    def close_parenthesis(self):
        self._append(")")
    
    def square_root(self):
        self._append("sqrt")

    def power(self):
        self._append("**")
    
    def compute_result(self) -> Number:
        try:
            result = eval(self.expression, MATH_FUNCTIONS)
            if isinstance(result, Number):
                self.expression = str(result)
                return result
            else:
                raise ValueError("Result is not a number: " + str(result))
        except Exception as e:
            expression = self.expression
            self.expression = ""
            raise ValueError("Invalid expression: " + expression) from e
