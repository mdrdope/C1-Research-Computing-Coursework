

import unittest
from dual_autodiff.dual import Dual
import math

class TestDual(unittest.TestCase):
    
    def test_initialization(self):
        try:
            x = Dual(2.0, 1.0)
            self.assertEqual(x.real, 2.0)
            self.assertEqual(x.dual, 1.0)
            print("test_initialization success")
        except AssertionError as e:
            print(f"test_initialization failed: real={x.real}, dual={x.dual}")
            raise e
    
    def test_addition_dual_dual(self):
        try:
            x = Dual(2.0, 1.0)
            y = Dual(3.0, 2.0)
            z = x + y
            self.assertEqual(z.real, 5.0)
            self.assertEqual(z.dual, 3.0)
            print("test_addition_dual_dual success")
        except AssertionError as e:
            print(f"test_addition_dual_dual failed: z.real={z.real}, z.dual={z.dual}")
            raise e
    
    def test_addition_dual_scalar(self):
        try:
            x = Dual(2.0, 1.0)
            scalar = 5.0
            z = x + scalar
            self.assertEqual(z.real, 7.0)
            self.assertEqual(z.dual, 1.0)
            print("test_addition_dual_scalar success")
        except AssertionError as e:
            print(f"test_addition_dual_scalar failed: z.real={z.real}, z.dual={z.dual}")
            raise e
    
    def test_addition_scalar_dual(self):
        try:
            scalar = 5.0
            x = Dual(2.0, 1.0)
            z = scalar + x
            self.assertEqual(z.real, 7.0)
            self.assertEqual(z.dual, 1.0)
            print("test_addition_scalar_dual success")
        except AssertionError as e:
            print(f"test_addition_scalar_dual failed: z.real={z.real}, z.dual={z.dual}")
            raise e
    
    def test_subtraction_dual_dual(self):
        try:
            x = Dual(5.0, 3.0)
            y = Dual(2.0, 1.0)
            z = x - y
            self.assertEqual(z.real, 3.0)
            self.assertEqual(z.dual, 2.0)
            print("test_subtraction_dual_dual success")
        except AssertionError as e:
            print(f"test_subtraction_dual_dual failed: z.real={z.real}, z.dual={z.dual}")
            raise e
    
    def test_subtraction_dual_scalar(self):
        try:
            x = Dual(5.0, 3.0)
            scalar = 2.0
            z = x - scalar
            self.assertEqual(z.real, 3.0)
            self.assertEqual(z.dual, 3.0)
            print("test_subtraction_dual_scalar success")
        except AssertionError as e:
            print(f"test_subtraction_dual_scalar failed: z.real={z.real}, z.dual={z.dual}")
            raise e
    
    def test_subtraction_scalar_dual(self):
        try:
            scalar = 5.0
            x = Dual(2.0, 1.0)
            z = scalar - x
            self.assertEqual(z.real, 3.0)
            self.assertEqual(z.dual, -1.0)
            print("test_subtraction_scalar_dual success")
        except AssertionError as e:
            print(f"test_subtraction_scalar_dual failed: z.real={z.real}, z.dual={z.dual}")
            raise e
    
    def test_multiplication_dual_dual(self):
        try:
            x = Dual(2.0, 1.0)
            y = Dual(3.0, 2.0)
            z = x * y
            self.assertEqual(z.real, 6.0)
            self.assertEqual(z.dual, 7.0)
            print("test_multiplication_dual_dual success")
        except AssertionError as e:
            print(f"test_multiplication_dual_dual failed: z.real={z.real}, z.dual={z.dual}")
            raise e
    
    def test_multiplication_dual_scalar(self):
        try:
            x = Dual(2.0, 1.0)
            scalar = 5.0
            z = x * scalar
            self.assertEqual(z.real, 10.0)
            self.assertEqual(z.dual, 5.0)
            print("test_multiplication_dual_scalar success")
        except AssertionError as e:
            print(f"test_multiplication_dual_scalar failed: z.real={z.real}, z.dual={z.dual}")
            raise e
    
    def test_multiplication_scalar_dual(self):
        try:
            scalar = 5.0
            x = Dual(2.0, 1.0)
            z = scalar * x
            self.assertEqual(z.real, 10.0)
            self.assertEqual(z.dual, 5.0)
            print("test_multiplication_scalar_dual success")
        except AssertionError as e:
            print(f"test_multiplication_scalar_dual failed: z.real={z.real}, z.dual={z.dual}")
            raise e
    
    def test_division_dual_dual(self):
        try:
            x = Dual(6.0, 7.0)
            y = Dual(3.0, 2.0)
            z = x / y
            self.assertEqual(z.real, 2.0)
            self.assertAlmostEqual(z.dual, (7*3 - 6*2) / 9)
            print("test_division_dual_dual success")
        except AssertionError as e:
            print(f"test_division_dual_dual failed: z.real={z.real}, z.dual={z.dual}")
            raise e
    
    def test_division_dual_scalar(self):
        try:
            x = Dual(6.0, 7.0)
            scalar = 3.0
            z = x / scalar
            self.assertEqual(z.real, 2.0)
            self.assertEqual(z.dual, 7.0 / 3.0)
            print("test_division_dual_scalar success")
        except AssertionError as e:
            print(f"test_division_dual_scalar failed: z.real={z.real}, z.dual={z.dual}")
            raise e
    
    def test_division_scalar_dual(self):
        try:
            scalar = 6.0
            x = Dual(3.0, 2.0)
            z = scalar / x
            self.assertEqual(z.real, 2.0)
            self.assertAlmostEqual(z.dual, (-6.0 * 2.0) / (3.0 ** 2))
            print("test_division_scalar_dual success")
        except AssertionError as e:
            print(f"test_division_scalar_dual failed: z.real={z.real}, z.dual={z.dual}")
            raise e
    
    def test_power_dual_scalar(self):
        try:
            x = Dual(2.0, 1.0)
            z = x ** 3
            self.assertEqual(z.real, 8.0)
            self.assertEqual(z.dual, 12.0)
            print("test_power_dual_scalar success")
        except AssertionError as e:
            print(f"test_power_dual_scalar failed: z.real={z.real}, z.dual={z.dual}")
            raise e
    def test_power_dual_dual(self):
        try:
            x = Dual(2.0, 1.0)
            y = Dual(3.0, 0.5)
            
            z = x ** y
            
            expected_real = 2.0 ** 3.0  # 8.0
            expected_dual = (2.0 ** 3.0) * ((3.0 * 1.0) / 2.0 + 0.5 * math.log(2.0))  # 8 * (1.5 + 0.5*0.69314718056)
            expected_dual = 8.0 * (1.5 + 0.5 * math.log(2.0))
            
            self.assertAlmostEqual(z.real, expected_real, places=7)
            self.assertAlmostEqual(z.dual, expected_dual, places=7)
            print("test_power_dual_dual success")
        except AssertionError as e:
            print(f"test_power_dual_dual failed: z.real={z.real}, z.dual={z.dual}")
            raise e
        

    def test_power_scalar_dual(self):
        try:
            a = 2.0
            y = Dual(3.0, 0.5)
            
            z = Dual(a, 0.0) ** y 
            
            expected_real = a ** y.real  # 2.0 ** 3.0 = 8.0
            expected_dual = (a ** y.real) * (y.dual * math.log(a))  # 8.0 * (0.5 * ln2)
            expected_dual = 8.0 * (0.5 * math.log(2.0))
            
            self.assertAlmostEqual(z.real, expected_real, places=7)
            self.assertAlmostEqual(z.dual, expected_dual, places=7)
            print("test_power_scalar_dual success")
        except AssertionError as e:
            print(f"test_power_scalar_dual failed: z.real={z.real}, z.dual={z.dual}")
            raise e
        
    def test_sin(self):
        try:
            x = Dual(math.pi/2, 1.0)
            y = x.sin()
            self.assertAlmostEqual(y.real, math.sin(math.pi/2))
            self.assertAlmostEqual(y.dual, math.cos(math.pi/2))
            print("test_sin success")
        except AssertionError as e:
            print(f"test_sin failed: y.real={y.real}, y.dual={y.dual}")
            raise e
    
    def test_log(self):
        try:
            x = Dual(math.e, 1.0)
            y = x.log()
            self.assertAlmostEqual(y.real, 1.0)
            self.assertAlmostEqual(y.dual, 1 / math.e)
            print("test_log success")
        except AssertionError as e:
            print(f"test_log failed: y.real={y.real}, y.dual={y.dual}")
            raise e
    
    def test_exp(self):
        try:
            x = Dual(1.0, 1.0)
            y = x.exp()
            self.assertAlmostEqual(y.real, math.exp(1.0))
            self.assertAlmostEqual(y.dual, math.exp(1.0))
            print("test_exp success")
        except AssertionError as e:
            print(f"test_exp failed: y.real={y.real}, y.dual={y.dual}")
            raise e
    
    def test_sqrt(self):
        try:
            x = Dual(4.0, 1.0)
            y = x.sqrt()
            self.assertEqual(y.real, 2.0)
            self.assertEqual(y.dual, 0.25)
            print("test_sqrt success")
        except AssertionError as e:
            print(f"test_sqrt failed: y.real={y.real}, y.dual={y.dual}")
            raise e
    
    def test_negation(self):
        try:
            x = Dual(2.0, 1.0)
            y = -x
            self.assertEqual(y.real, -2.0)
            self.assertEqual(y.dual, -1.0)
            print("test_negation success")
        except AssertionError as e:
            print(f"test_negation failed: y.real={y.real}, y.dual={y.dual}")
            raise e

if __name__ == '__main__':
    unittest.main()

