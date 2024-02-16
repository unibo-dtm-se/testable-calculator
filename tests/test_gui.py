import unittest
from calculator.ui.gui import CalculatorApp


class TestCalculatorGui(unittest.TestCase):
    def setUp(self):
        self.app = CalculatorApp()
        self.app._run_prepare()

    def test_composing_expression(self):
        self.app.button("1").trigger_action()
        self.app.button("+").trigger_action()
        self.app.button("2").trigger_action()
        self.app.display.text = "1+2"