import unittest
import string_calculator


class CalculatorTest(unittest.TestCase):
  def givenEmptyStringZeroIsExpected(self):
    self.assertTrue(string_calculator.add("") == 0)
    
#Code Implementation

def add(str):
  if str=="":
    return 0

