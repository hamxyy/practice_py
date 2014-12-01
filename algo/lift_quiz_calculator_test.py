import random
import unittest
from lift_quiz_calculator import *

calc = Calculator()
L = [1,4,7,10,40,100,231]

class TestCalculatorFunctions(unittest.TestCase):

	def test_actual_time(self):
		self.assertEqual(calc.lift_time(1, L), 0)
		self.assertEqual(calc.lift_time(2, L), 4)
		self.assertEqual(calc.lift_time(3, L), 8)
		self.assertEqual(calc.lift_time(4, L), 12)
		self.assertEqual(calc.lift_time(5, L), 26)
		self.assertEqual(calc.lift_time(6, L), 30)
		self.assertEqual(calc.lift_time(7, L), 34)
		self.assertEqual(calc.lift_time(40, L), 186)
	
	def test_find_fastest_route(self):
		self.assertEqual(calc.find_fastest_route(1, L)['stop'], 1)
		self.assertEqual(calc.find_fastest_route(1, L)['time'], 0)
		self.assertEqual(calc.find_fastest_route(2, L)['stop'], 1)
		self.assertEqual(calc.find_fastest_route(2, L)['time'], 20)
		self.assertEqual(calc.find_fastest_route(4, L)['stop'], 4)
		self.assertEqual(calc.find_fastest_route(4, L)['time'], 12)
		self.assertEqual(calc.find_fastest_route(39, L)['stop'], 40)
		self.assertEqual(calc.find_fastest_route(39, L)['time'], 206)
		self.assertEqual(calc.find_fastest_route(101, L)['stop'], 100)

	def test_calculate_latest_time(self):
		S = [4,10,100,231]
		self.assertEqual(calc.calculate_latest_time(L, S)['stop'], 231)
		self.assertEqual(calc.calculate_latest_time(L, S)['dest'], 231)

	def test_bin_to_str(self):
		self.assertEqual(bin_to_str(0, 8), "00000000")
		self.assertEqual(bin_to_str(1, 8), "00000001")
		self.assertEqual(bin_to_str(2, 8), "00000010")
		self.assertEqual(bin_to_str(3, 8), "00000011")
		self.assertEqual(bin_to_str(4, 8), "00000100")
		self.assertEqual(bin_to_str(5, 8), "00000101")
		self.assertEqual(bin_to_str(6, 8), "00000110")
		self.assertEqual(bin_to_str(7, 8), "00000111")
		self.assertEqual(bin_to_str(8, 8), "00001000")

	def test_enumerate_all_possibilities(self):
		# no stop is not an option. So here there will be only 127 returned.
		self.assertEqual(len(calc.enumerate_all_possibilities(L)), 2**7-1)

	def test_find_fastest_route(self):
		self.assertEqual(calc.find_from_all(L)["dest"], 231)
		self.assertEqual(calc.find_from_all(L)["stop"], 231)

    #~ def test_shuffle(self):
        #~ # make sure the shuffled sequence does not lose any elements
        #~ random.shuffle(self.seq)
        #~ self.seq.sort()
        #~ self.assertEqual(self.seq, list(range(10)))

        #~ # should raise an exception for an immutable sequence
        #~ self.assertRaises(TypeError, random.shuffle, (1,2,3))

    #~ def test_choice(self):
        #~ element = random.choice(self.seq)
        #~ self.assertTrue(element in self.seq)

    #~ def test_sample(self):
        #~ with self.assertRaises(ValueError):
            #~ random.sample(self.seq, 20)
        #~ for element in random.sample(self.seq, 5):
            #~ self.assertTrue(element in self.seq)

if __name__ == '__main__':
    unittest.main()