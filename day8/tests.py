import unittest
from collections import defaultdict
from code import *

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        registers = defaultdict(lambda : 0)

    def test_testComp(self):
        self.assertTrue(evalComp("xa","==","0"))
        self.assertFalse(evalComp("xa",">=","1"))
        self.assertTrue(evalComp("xa","<=","0"))

    def test_evalLine(self):
        line = "b inc 5 if a > 1"
        evalLine(line)
        self.assertEqual(registers["b"],0)
        self.assertEqual(registers["a"],0)
        line = "a inc 1 if b < 5"
        evalLine(line)
        self.assertEqual(registers["a"],1)
        line = "c dec -10 if a >= 1"
        evalLine(line)
        line = "c inc -20 if c == 10"
        evalLine(line)
        self.assertEqual(registers["c"],-10)

    def test_max(self):
        registers["low"] = -252352
        registers["med"] = 251
        registers["high"] = 5252252515125
        regName, regValue = getMax()
        self.assertEqual(regName, "high")
        self.assertEqual(regValue, 5252252515125)

    def test_highest(self):
        lines = ["b inc 5 if a > 1",
                "a inc 1 if b < 5",
                "c dec -10 if a >= 1",
                "c inc -20 if c == 10"]
        for line in lines:
            evalLine(line)
        regName, regValue = getHighest()
        self.assertEqual(regValue,10)
        self.assertEqual(regName, "c")

if __name__ == '__main__':
    unittest.main()
