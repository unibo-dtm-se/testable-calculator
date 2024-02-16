import io
import unittest
from calculator.ui.cli import main


class TestCalculatorCli(unittest.TestCase):
    def setUp(self):
        self.output = io.StringIO()

    def test_cli_with_sliced_expression(self):
        main(["1", "+", "2"], output=self.output)
        self.assertEqual("3\n", self.output.getvalue())

    def test_cli_with_invalid_expression(self):
        main(["1", "+"], output=self.output)
        self.assertEqual("Invalid expression: 1 +\n", self.output.getvalue())

    def test_cli_with_single_expression(self):
        main(["3-2"], output=self.output)
        self.assertEqual("1\n", self.output.getvalue())
