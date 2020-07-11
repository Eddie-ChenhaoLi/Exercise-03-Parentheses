import unittest
import parentheses


class TestParentheses(unittest.TestCase):

    def test_is_balanced(self):
        self.assertEqual(parentheses.is_balanced('[({})]'), True)
        self.assertEqual(parentheses.is_balanced('{()}[[{}]]'), True)
        self.assertEqual(parentheses.is_balanced('{{)(}}'), False)
        self.assertEqual(parentheses.is_balanced('({)}'), False)
