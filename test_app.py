import unittest

from app import add_numbers, get_message


class TestApplication(unittest.TestCase):

    def test_get_message(self):
        self.assertEqual(
            get_message(),
            "Hello from DVP Week 12 CI/CD Pipeline!"
        )

    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-2, -3), -5)


if __name__ == "__main__":
    unittest.main()
