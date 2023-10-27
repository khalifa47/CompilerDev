import unittest
from lexer import lexer


class TestLexer(unittest.TestCase):
    def test_assignment_and_expression(self):
        code = "weka x kuwa 42 + 3\n"
        expected_tokens = [
            ('KEYWORD', 'weka', 1),
            ('IDENTIFIER', 'x', 1),
            ('KEYWORD', 'kuwa', 1),
            ('NUMBER', '42', 1),
            ('OPERATOR', '+', 1),
            ('NUMBER', '3', 1),
            ('EOF', '', 2)
        ]

        self.assertEqual(lexer(code), expected_tokens)

    def test_if_statement(self):
        code = """ikiwa x ni sawa na 10 basi
                    chapisha "sawa"
                mwisho"""
        expected_tokens = [
            ('KEYWORD', 'ikiwa', 1),
            ('IDENTIFIER', 'x', 1),
            ('COMPARISON', 'ni sawa na', 1),
            ('NUMBER', '10', 1),
            ('KEYWORD', 'basi', 1),
            ('KEYWORD', 'chapisha', 2),
            ('STRING', '"sawa"', 2),
            ('KEYWORD', 'mwisho', 3),
            ('EOF', '', 3)
        ]
        self.assertEqual(lexer(code), expected_tokens)


if __name__ == "__main__":
    unittest.main()
