
# import unittest
# from dual_autodiff.dual import Dual
# import math

# class TestDual(unittest.TestCase):
    
#     def test_initialization(self):
#         x = Dual(2.0, 1.0)
#         self.assertEqual(x.real, 2.0)
#         self.assertEqual(x.dual, 1.0)
    
#     def test_addition(self):
#         x = Dual(2.0, 1.0)
#         y = Dual(3.0, 2.0)
#         z = x + y
#         self.assertEqual(z.real, 5.0)
#         self.assertEqual(z.dual, 3.0)
    
#     def test_subtraction(self):
#         x = Dual(5.0, 3.0)
#         y = Dual(2.0, 1.0)
#         z = x - y
#         self.assertEqual(z.real, 3.0)
#         self.assertEqual(z.dual, 2.0)
    
#     def test_multiplication(self):
#         x = Dual(2.0, 1.0)
#         y = Dual(3.0, 2.0)
#         z = x * y
#         self.assertEqual(z.real, 6.0)
#         self.assertEqual(z.dual, 7.0)
    
#     def test_division(self):
#         x = Dual(6.0, 7.0)
#         y = Dual(3.0, 2.0)
#         z = x / y
#         self.assertEqual(z.real, 2.0)
#         self.assertAlmostEqual(z.dual, (7*3 - 6*2) / 9)
    
#     def test_sin(self):
#         x = Dual(math.pi/2, 1.0)
#         y = x.sin()
#         self.assertAlmostEqual(y.real, math.sin(math.pi/2))
#         self.assertAlmostEqual(y.dual, math.cos(math.pi/2))
    
#     def test_log(self):
#         x = Dual(math.e, 1.0)
#         y = x.log()
#         self.assertAlmostEqual(y.real, 1.0)
#         self.assertAlmostEqual(y.dual, 1 / math.e)
    
#     def test_power(self):
#         x = Dual(2.0, 1.0)
#         y = x ** 3
#         self.assertEqual(y.real, 8.0)
#         self.assertEqual(y.dual, 12.0)

# if __name__ == '__main__':
#     unittest.main()
