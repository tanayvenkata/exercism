import unittest
from bottle_song import recite

class TestBottleSong(unittest.TestCase):
    def test_recite_default(self):
        # Test the function with standard input
        result = recite(start=10)
        expected_output = [
            "Ten green bottles hanging on the wall,",
            "Ten green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be nine green bottles hanging on the wall.",
        ]
        self.assertEqual(result, expected_output)

    def test_recite_lower_start(self):
        # Test the function with lower start
        result = recite(start=3)
        expected_output = [
            "Three green bottles hanging on the wall,",
            "Three green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be two green bottles hanging on the wall.",
        ]
        self.assertEqual(result, expected_output)

    def test_recite_one_bottle(self):
        # Test the function with one bottle
        result = recite(start=1)
        expected_output = [
            "One green bottle hanging on the wall,",
            "One green bottle hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be no green bottles hanging on the wall.",
        ]
        self.assertEqual(result, expected_output)

    def test_recite_two_bottle(self):
    # Test the function with two bottles
        result = recite(start=2)
        expected_output = [
            "Two green bottles hanging on the wall,",
            "Two green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be one green bottle hanging on the wall.",
        ]
        self.assertEqual(result, expected_output)

    def test_recite_ten_bottle_two_take(self):
    # Test the function with two bottles
        result = recite(start=10, take=2)
        expected_output = [
            "Ten green bottles hanging on the wall,",
            "Ten green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be nine green bottles hanging on the wall.",
            "",
            "Nine green bottles hanging on the wall,",
            "Nine green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be eight green bottles hanging on the wall.",
        ]
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
