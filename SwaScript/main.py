from lexer import lexer
from parse import Parser
from interpreter import Interpreter

test_code = """kwa kila i katika 1 hadi 5 fanya
                    chapisha i
                mwisho"""

test_tokens = lexer(test_code)
print("Tokens:")
print(test_tokens)

parser = Parser(test_tokens)
ast = parser.parse_program()
print("AST:")
print(ast)

interpreter = Interpreter()
res = interpreter.interpret_program(ast)
print("Result:")
print(res)
