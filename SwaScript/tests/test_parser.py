import unittest
from lexer import lexer
from parse import Parser


class TestParser(unittest.TestCase):
    def test_print_statement(self):
        code = '''chapisha "Habari, Dunia!"
                chapisha 42
                chapisha var'''
        expected_ast = [
            ('print', ('string', 'Habari, Dunia!'), 1),
            ('print', ('number', 42.0), 2),
            ('print', ('identifier', 'var'), 3)
        ]

        tokens = lexer(code)
        parser = Parser(tokens)
        ast = parser.parse_program()
        self.assertEqual(ast, expected_ast)

    def test_assignment_and_expression(self):
        code = "weka x kuwa 42 - 3\n"
        expected_ast = [
            ('assignment', 'x', ('operator', '-', ('number', 42.0), ('number', 3.0)), 1)]

        tokens = lexer(code)
        parser = Parser(tokens)
        ast = parser.parse_program()
        self.assertEqual(ast, expected_ast)

    def test_if_statement(self):
        code = """ikiwa x ni sawa na 10 basi
                    chapisha "sawa"
                mwisho"""
        expected_ast = [('if', ('comparison', 'ni sawa na', ('identifier', 'x'), ('number', 10.0)), [
                         ('print', ('string', 'sawa'), 2)], 1)]

        tokens = lexer(code)
        parser = Parser(tokens)
        ast = parser.parse_program()
        self.assertEqual(ast, expected_ast)

    def test_loop(self):
        code = """kwa kila i katika 1 hadi 5 fanya
                    chapisha i
                mwisho"""
        expected_ast = [('forloop', 'i', (('number', 1.0), ('number', 5.0)), [
                         ('print', ('identifier', 'i'), 2)], 1)]

        tokens = lexer(code)
        parser = Parser(tokens)
        ast = parser.parse_program()
        self.assertEqual(ast, expected_ast)


if __name__ == "__main__":
    unittest.main()
