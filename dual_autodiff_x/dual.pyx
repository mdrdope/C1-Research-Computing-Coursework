#cython: language_level=3
from libc.math cimport sin as c_sin, cos as c_cos, tan as c_tan, exp as c_exp, log as c_log, pow as c_pow

cdef class Dual:
    cdef double _real  
    cdef double _dual  

    def __init__(self, double real, double dual=1.0):
        self._real = real  
        self._dual = dual  

    def __repr__(self):
        return f"Dual(real={self._real}, dual={self._dual})"

    @property
    def real(self): 
        '''
        Returns:
            double: The real part of the dual number.
        '''
        return self._real

    @real.setter
    def real(self, value):
        '''
        Sets the real part of the dual number.
        '''
        self._real = value

    @property
    def dual(self):
        '''
        Returns:
            double: The dual part of the dual number.
        '''
        return self._dual

    @dual.setter
    def dual(self, value):
        '''
        Sets the dual part of the dual number.
        '''
        self._dual = value

    def __add__(self, other):
        if isinstance(other, Dual):
            return Dual(self.real + other.real, self.dual + other.dual)
        elif isinstance(other, (float, int)):
            return Dual(self.real + other, self.dual)
        else:
            raise TypeError(f"Unsupported operand type(s) for +: 'Dual' and '{type(other).__name__}'")

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Dual):
            return Dual(self.real - other.real, self.dual - other.dual)
        elif isinstance(other, (float, int)):
            return Dual(self.real - other, self.dual)
        else:
            raise TypeError(f"Unsupported operand type(s) for -: 'Dual' and '{type(other).__name__}'")

    def __rsub__(self, other):
        if isinstance(other, (float, int)):
            return Dual(other - self.real, -self.dual)
        else:
            raise TypeError(f"Unsupported operand type(s) for -: '{type(other).__name__}' and 'Dual'")

    def __mul__(self, other):
        if isinstance(other, Dual):
            return Dual(self.real * other.real, self.real * other.dual + self.dual * other.real)
        elif isinstance(other, (float, int)):
            return Dual(self.real * other, self.dual * other)
        else:
            raise TypeError(f"Unsupported operand type(s) for *: 'Dual' and '{type(other).__name__}'")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        cdef double real_part, dual_part
        if isinstance(other, Dual):
            if other.real == 0.0:
                raise ZeroDivisionError("Division by zero: real part of the divisor is zero.")
            real_part = self.real / other.real
            dual_part = (self.dual * other.real - self.real * other.dual) / (other.real * other.real)
            return Dual(real_part, dual_part)
        elif isinstance(other, (float, int)):
            if other == 0.0:
                raise ZeroDivisionError("Division by zero.")
            return Dual(self.real / other, self.dual / other)
        else:
            raise TypeError(f"Unsupported operand type(s) for /: 'Dual' and '{type(other).__name__}'")

    def __rtruediv__(self, other):
        cdef double real_part, dual_part
        if self.real == 0.0:
            raise ZeroDivisionError("Division by zero in dual number.")
        if isinstance(other, (float, int)):
            real_part = other / self.real
            dual_part = (-other * self.dual) / (self.real * self.real)
            return Dual(real_part, dual_part)
        else:
            raise TypeError(f"Unsupported operand type(s) for /: '{type(other).__name__}' and 'Dual'")

    def __pow__(self, power):
        cdef double real, dual, log_real
        if isinstance(power, (float, int)):
            if self.real < 0.0 and not isinstance(power, int):
                raise ValueError("Real part must be non-negative for non-integer exponents.")
            real = c_pow(self.real, power)
            dual = power * c_pow(self.real, power - 1.0) * self.dual
            return Dual(real, dual)
        elif isinstance(power, Dual):
            if self.real <= 0.0:
                raise ValueError("Real part must be positive for dual exponentiation.")
            log_real = c_log(self.real)
            real = c_pow(self.real, power.real)
            dual = real * (power.dual * log_real + (power.real * self.dual) / self.real)
            return Dual(real, dual)
        else:
            raise TypeError(f"Unsupported exponent type: '{type(power).__name__}'")

    def __neg__(self):
        return Dual(-self.real, -self.dual)

    cpdef sin(self):
        cdef double sin_real = c_sin(self.real)
        cdef double cos_real = c_cos(self.real)
        return Dual(sin_real, cos_real * self.dual)

    cpdef cos(self):
        cdef double cos_real = c_cos(self.real)
        cdef double sin_real = c_sin(self.real)
        return Dual(cos_real, -sin_real * self.dual)

    cpdef tan(self):
        cdef double sin_real = c_sin(self.real)
        cdef double cos_real = c_cos(self.real)
        if cos_real == 0.0:
            raise ValueError("Undefined tan at this real part.")
        return Dual(sin_real / cos_real, self.dual / (cos_real * cos_real))

    cpdef exp(self):
        cdef double exp_real = c_exp(self.real)
        return Dual(exp_real, exp_real * self.dual)

    cpdef log(self):
        if self.real <= 0.0:
            raise ValueError("Log undefined for non-positive real parts.")
        cdef double log_real = c_log(self.real)
        return Dual(log_real, self.dual / self.real)

    cpdef sqrt(self):
        return self.__pow__(0.5)
