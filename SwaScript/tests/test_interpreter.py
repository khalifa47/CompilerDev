import unittest
from lexer import lexer
from parse import Parser
from interpreter import Interpreter


class TestInterpreter(unittest.TestCase):
    def test_assignment_and_expression(self):
        code = '''
                weka jina kuwa "SwaScript"
                chapisha jina
                '''
        expected_res = "SwaScript"

        tokens = lexer(code)
        parser = Parser(tokens)
        ast = parser.parse_program()
        interpreter = Interpreter()
        res = interpreter.interpret_program(ast)
        self.assertEqual(res, expected_res)

    def test_if_statement(self):
        code = """weka x kuwa 20
                    ikiwa x kubwa kuliko 10 basi
                        chapisha "sawa"
                    mwisho"""
        expected_res = "sawa"

        tokens = lexer(code)
        parser = Parser(tokens)
        ast = parser.parse_program()
        interpreter = Interpreter()
        res = interpreter.interpret_program(ast)
        self.assertEqual(res, expected_res)

    def test_loop(self):
        code = """kwa kila i katika 1 hadi 5 fanya
                    chapisha i
                mwisho"""
        expected_res = [1, 2, 3, 4, 5]

        tokens = lexer(code)
        parser = Parser(tokens)
        ast = parser.parse_program()
        interpreter = Interpreter()
        res = interpreter.interpret_program(ast)
        self.assertEqual(res, expected_res)


if __name__ == "__main__":
    unittest.main()
