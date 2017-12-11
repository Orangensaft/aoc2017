import unittest
from code import *

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        pass

    def test_countGroups(self):
        tests = [("{}" , 1),
        ("{{{}}}", 3),
        ("{{},{}}", 3),
        ("{{{},{},{{}}}}", 6)]
        for stream, count in tests:
            groupCount, score, deleted = analyzeStream(stream)
            self.assertEqual(count, groupCount)

    def test_garbageGroups(self):
        tests = [("{<{},{},{{}}>}", 1),
        ("{<a>,<a>,<a>,<a>}", 1),
        ("{{<a>},{<a>},{<a>},{<a>}}", 5),
        ("{{<!>},{<!>},{<!>},{<a>}}", 2)]
        for stream, count in tests:
            groupCount, score, deleted = analyzeStream(stream)
            self.assertEqual(count, groupCount)

    def test_groupScore(self):
        tests = [("{}" , 1),
        ("{{{}}}", 6),
        ("{{},{}}", 5),
        ("{{{},{},{{}}}}", 16),
        ("{<a>,<a>,<a>,<a>}", 1),
        ("{{<ab>},{<ab>},{<ab>},{<ab>}}", 9),
        ("{{<!!>},{<!!>},{<!!>},{<!!>}}", 9),
        ("{{<a!>},{<a!>},{<a!>},{<ab>}}", 3)]
        for stream, score in tests:
            groupCount, groupScore, deleted = analyzeStream(stream)
            self.assertEqual(score, groupScore)

    def test_delCount(self):
        tests = [
            ("<>",0),
            ("<random characters>",17),
            ("<<<<>",3),
            ("<{!>}>",2),
            ("<!!>",0),
            ("<!!!>>",0),
            ("<{o\"i!a,<{i<a>",10),
        ]
        for stream, count in tests:
            groupCount, groupScore, deleted = analyzeStream(stream)
            self.assertEqual(deleted, count)

if __name__ == '__main__':
    unittest.main()
