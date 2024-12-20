import math

class Dual:
    """
    A class to represent dual numbers for automatic differentiation.

    Dual numbers are represented as:
        x = a + bE
    where E is the dual unit with the property E * E = 0.

    Attributes:
        real (float): The real part of the dual number.

        dual (float): The dual part of the dual number.
    """
    
    # Methods:
    # __add__(other):
    #     Adds two dual numbers or a dual number with a scalar.

    # __sub__(other):
    #     Subtracts two dual numbers or a dual number with a scalar.

    # __mul__(other):
    #     Multiplies two dual numbers or a dual number with a scalar.

    # __truediv__(other):
    #     Divides a dual number by another dual number or a scalar.

    # __pow__(power):
    #     Raises a dual number to a scalar or another dual number.

    # __neg__():
    #     Negates a dual number.

    # sin():
    #     Computes the sine of the dual number.

    # cos():
    #     Computes the cosine of the dual number.

    # tan():
    #     Computes the tangent of the dual number.

    # exp():
    #     Computes the exponential of the dual number.

    # log():
    #     Computes the natural logarithm of the dual number.

    # sqrt():
    #     Computes the square root of the dual number.

    def __init__(self, real: float, dual: float = 1.0):
        """
        Initialize a Dual number.

        Input:
            real (float): The real part of the dual number.

            dual (float, optional): The dual part of the dual number. Defaults to 1.0 for differential propagation.
        """
        self.real = real
        self.dual = dual

    def __repr__(self) -> str:
        """
        Return the string representation of the dual number.

        Returns:
            str: String representation in the format Dual(real=a, dual=b).
        """
        return f'Dual(real={self.real}, dual={self.dual})'

    def __add__(self, other):
        """
        Add this dual number to another dual number or scalar.

        Input:
            self (Dual): A dual number represented as a + bE.

            other (Dual, float, int): The other operand, represented as:
                - A scalar s.
                - A dual number c + dE.

        Returns:
            Dual:
                If `other` is a scalar s:
                    Real part: a + s

                    Dual part: b

                If `other` is a Dual number c + dE:
                    Real part: a + c

                    Dual part: b + d

        Raises:
            TypeError: If `other` is not a Dual number, float, or int.
        """
        if isinstance(other, Dual):
            return Dual(self.real + other.real, self.dual + other.dual)
        elif isinstance(other, (float, int)):
            return Dual(self.real + other, self.dual)
        else:
            raise TypeError(f"Unsupported operand type(s) for +: 'Dual' and '{type(other).__name__}'")

    __radd__ = __add__

    def __sub__(self, other):
        """
        Subtract another dual number or scalar from this dual number.

        Input:
            self (Dual): A dual number represented as a + bE.

            other (Dual, float, int): The other operand, represented as:
                - A scalar s.
                - A dual number c + dE.

        Returns:
            Dual:
                If `other` is a scalar s:
                    Real part: a - s

                    Dual part: b

                If `other` is a Dual number c + dE:
                    Real part: a - c

                    Dual part: b - d

        Raises:
            TypeError: If `other` is not a Dual number, float, or int.
        """
        if isinstance(other, Dual):
            return Dual(self.real - other.real, self.dual - other.dual)
        elif isinstance(other, (float, int)):
            return Dual(self.real - other, self.dual)
        else:
            raise TypeError(f"Unsupported operand type(s) for -: 'Dual' and '{type(other).__name__}'")

    def __rsub__(self, other):
        """
        Subtract this dual number from a scalar.

        Input:
            self (Dual): A dual number represented as a + bE.

            other (float, int): The scalar operand s.

        Returns:
            Dual:
                Real part: s - a

                Dual part: -b

        Raises:
            TypeError: If `other` is not a float or int.
        """
        if isinstance(other, (float, int)):
            return Dual(other - self.real, -self.dual)
        else:
            raise TypeError(f"Unsupported operand type(s) for -: '{type(other).__name__}' and 'Dual'")


    def __mul__(self, other):
        """
        Multiply this dual number by another dual number or scalar.

        Input:
            self (Dual): A dual number represented as a + bE.

            other (Dual, float, int): The other operand, represented as:
                - A scalar s.
                - A dual number c + dE.

        Returns:
            Dual:
                If `other` is a scalar s:
                    Real part: a * s

                    Dual part: b * s

                If `other` is a Dual number c + dE:
                    Real part: a * c

                    Dual part: a * d + b * c

        Raises:
            TypeError: If `other` is not a Dual number, float, or int.
        """
        if isinstance(other, Dual):
            return Dual(self.real * other.real, self.real * other.dual + self.dual * other.real)
        elif isinstance(other, (float, int)):
            return Dual(self.real * other, self.dual * other)
        else:
            raise TypeError(f"Unsupported operand type(s) for *: 'Dual' and '{type(other).__name__}'")

    __rmul__ = __mul__

    def __truediv__(self, other):
        """
        Divide this dual number by another dual number or scalar.

        Input:
            self (Dual): A dual number represented as a + bE.

            other (Dual, float, int): The divisor, represented as:
                - A scalar s.
                - A dual number c + dE.

        Returns:
            Dual:
                If `other` is a scalar s:
                    Real part: a / s

                    Dual part: b / s

                If `other` is a Dual number c + dE:
                    Real part: a / c

                    Dual part: (b * c - a * d) / c*c

        Raises:
            TypeError: If `other` is not a Dual number, float, or int.
            ZeroDivisionError: If dividing by zero (real part of `other` is zero).
        """
        if isinstance(other, Dual):
            if other.real == 0:
                raise ZeroDivisionError("Division by zero: real part of the divisor is zero.")
            real_part = self.real / other.real
            dual_part = (self.dual * other.real - self.real * other.dual) / (other.real ** 2)
            return Dual(real_part, dual_part)
        elif isinstance(other, (float, int)):
            if other == 0:
                raise ZeroDivisionError("Division by zero.")
            return Dual(self.real / other, self.dual / other)
        else:
            raise TypeError(f"Unsupported operand type(s) for /: 'Dual' and '{type(other).__name__}'")

    def __rtruediv__(self, other):
        """
        Divide a scalar by this dual number.

        Input:
            self (Dual): A dual number represented as a + bE.

            other (float, int): The numerator, represented as a scalar s.

        Returns:
            Dual:
                Real part: s / a

                Dual part: - (s * b) / a*a

        Raises:
            TypeError: If `other` is not a float or int.
            ZeroDivisionError: If dividing by a Dual number with zero real part (a = 0).
        """
        if self.real == 0:
            raise ZeroDivisionError("Division by zero in dual number.")
        if isinstance(other, (float, int)):
            real_part = other / self.real
            dual_part = (-other * self.dual) / (self.real ** 2)
            return Dual(real_part, dual_part)
        else:
            raise TypeError(f"Unsupported operand type(s) for /: '{type(other).__name__}' and 'Dual'")

    def __pow__(self, power):
        """
        Raise this dual number to a scalar or another dual number.

        Input:
            self (Dual): A dual number represented as a + bE.

            power (Dual, float, int): The exponent, represented as:
                - A scalar p.
                - A dual number c + dE.

        Returns:
            Dual: 
                If `power` is a scalar p:
                    Real part: a^p

                    Dual part: p * a^(p-1) * b

                If `power` is a Dual number c + dE:
                    Real part: a^c

                    Dual part: a^c * (c * b / a + d * log(a))

        Raises:
            TypeError: If `power` is not a Dual number, float, or int.
            ValueError: If a <= 0 and `power` is a Dual number.
        """

        if isinstance(power, (float, int)):
            if self.real < 0 and not isinstance(power, int):
                raise ValueError("Real part must be non-negative for non-integer exponents.")
            real = self.real ** power
            dual = power * (self.real ** (power - 1)) * self.dual
            return Dual(real, dual)
        elif isinstance(power, Dual):
            if self.real <= 0:
                raise ValueError("Real part must be positive for dual exponentiation.")
            log_a = math.log(self.real)
            real = self.real ** power.real
            dual = real * (power.dual * log_a + (power.real * self.dual) / self.real)
            return Dual(real, dual)
        else:
            raise TypeError(f"Unsupported exponent type: '{type(power).__name__}'")

    def __neg__(self):
        """
        Negate this dual number.

        Input:
            self (Dual): A dual number represented as a + bE.

        Returns:
            Dual:
                Real part: -a

                Dual part: -b
        """

        return Dual(-self.real, -self.dual)

    def sin(self):
        """
        Compute the sine of this dual number.

        Input:
            self (Dual): A dual number represented as a + bE.

        Returns:
            Dual:
                Real part: sin(a)

                Dual part: b * cos(a)

        Raises:
            TypeError: If `self` is not an instance of Dual.
        """
        if not isinstance(self, Dual):
            raise TypeError("Input must be a Dual number.")
        return Dual(math.sin(self.real), math.cos(self.real) * self.dual)

    def cos(self):
        """
        Compute the cosine of this dual number.

        Input:
            self (Dual): A dual number represented as a + bE.

        Returns:
            Dual:
                Real part: cos(a)

                Dual part: -b * sin(a)

        Raises:
            TypeError: If `self` is not an instance of Dual.
        """
        if not isinstance(self, Dual):
            raise TypeError("Input must be a Dual number.")
        return Dual(math.cos(self.real), -math.sin(self.real) * self.dual)

    def tan(self):
        """
        Compute the tangent of this dual number.

        Input:
            self (Dual): A dual number represented as a + bE.

        Returns:
            Dual:
                Real part: tan(a)

                Dual part: b / cos(a)*cos(a)

        Raises:
            TypeError: If `self` is not an instance of Dual.
            ValueError: If cos(a) is zero (tangent is undefined).
        """
        if not isinstance(self, Dual):
            raise TypeError("Input must be a Dual number.")
        cos_real = math.cos(self.real)
        if cos_real == 0:
            raise ValueError("Undefined tan at this real part.")
        return Dual(math.tan(self.real), self.dual / (cos_real ** 2))

    def exp(self):
        """
        Compute the exponential of this dual number.

        Input:
            self (Dual): A dual number represented as a + bE.

        Returns:
            Dual:
                Real part: exp(a)

                Dual part: b * exp(a)

        Raises:
            TypeError: If `self` is not an instance of Dual.
        """
        if not isinstance(self, Dual):
            raise TypeError("Input must be a Dual number.")
        exp_real = math.exp(self.real)
        return Dual(exp_real, exp_real * self.dual)

    def log(self):
        """
        Compute the natural logarithm of this dual number.

        Input:
            self (Dual): A dual number represented as a + bE.

        Returns:
            Dual:
                Real part: log(a)

                Dual part: b / a

        Raises:
            TypeError: If `self` is not an instance of Dual.
            ValueError: If a <= 0 (logarithm undefined).
        """
        if not isinstance(self, Dual):
            raise TypeError("Input must be a Dual number.")
        if self.real <= 0:
            raise ValueError("Log undefined for non-positive real parts.")
        return Dual(math.log(self.real), self.dual / self.real)

    def sqrt(self):
        """
        Compute the square root of this dual number by leveraging the __pow__ method.

        Input:
            self (Dual): A dual number represented as a + bE.

        Returns:
            Dual:
                Real part: sqrt(a)
                
                Dual part: b / (2 * sqrt(a))

        Raises:
            TypeError: If `self` is not an instance of Dual.
            ValueError: If a < 0 (square root undefined).
        """
        return self.__pow__(0.5)