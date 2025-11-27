import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method with various inputs."""
        # Basic positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 5), 15)

        # Including zero
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(7, 0), 7)

        # Negative numbers
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(-5, 3), -2)

        # Floats
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)

    def test_subtraction(self):
        """Test the subtract method with various inputs."""
        # Basic positive numbers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 5), 5)

        # Result negative
        self.assertEqual(self.calc.subtract(3, 5), -2)

        # Including zero
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)

        # Negative numbers
        self.assertEqual(self.calc.subtract(-5, -5), 0)
        self.assertEqual(self.calc.subtract(-5, 3), -8)

        # Floats
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)

    def test_multiplication(self):
        """Test the multiply method with various inputs."""
        # Basic positive numbers
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(10, 5), 50)

        # Including zero
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(7, 0), 0)

        # Negative numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)

        # Floats
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)

    def test_division_normal(self):
        """Test the divide method with valid, non-zero denominators."""
        # Basic division
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(10, 2), 5)

        # Result as float
        self.assertEqual(self.calc.divide(7, 2), 3.5)

        # Negative numbers
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(-6, -3), 2)

        # Floats
        self.assertEqual(self.calc.divide(5.0, 2.0), 2.5)

    def test_division_by_zero(self):
        """Test that divide returns None when dividing by zero."""
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        self.assertIsNone(self.calc.divide(-10, 0))


if __name__ == "__main__":
    unittest.main()
