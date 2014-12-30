import unittest

from skills1 import *

class TestListOperations(unittest.TestCase):

	def setUp(self):
		self.some_list = [3, 4, 2, 1, 5, 6]
		self.word_list = ["apple", "bit", "saucy", "red", "core", "seed", "new"]
		self.string_list = ["I", "went", "dancing", "last", "night."]
		self.numbers = [2, 4, 6, 8]

	def test_1_A_all_odd(self):
	    self.assertEqual(all_odd(self.some_list), [3, 1, 5])

	def test_1_B_all_even(self):
	    self.assertEqual(all_even(self.some_list), [4, 2, 6])

	def test_1_C_long_words(self):
	    self.assertEqual(long_words(self.word_list), ["apple", "saucy", "core", "seed"])

	def test_1_D_smallest(self):
	    self.assertEqual(smallest(self.some_list), 1)

	def test_1_E_largest(self):
	    self.assertEqual(largest(self.some_list), 6)

	def test_1_F_halvesies(self):
	    self.assertEqual(halvesies(some_list), [1.5, 2, 1, .5, 2.5, 3])

	def test_1_G_word_lengths(self):
	    self.assertEqual(word_lengths(self.word_list), [5, 3, 5, 3, 4, 4, 3])

	def test_1_H_sum_numbers(self):
	    self.assertEqual(sum_numbers(self.numbers), 20)

	def test_1_I_mult_numbers(self):
	    self.assertEqual(mult_numbers(self.numbers), 384)

	def test_1_J_join_strings(self):
	    self.assertEqual(join_strings(self.string_list), "I went dancing last night.")

	def test_1_K_average(self):
	    self.assertEqual(average(self.numbers), 5)
                                
                                
if __name__ == '__main__':
    unittest.main()                              
