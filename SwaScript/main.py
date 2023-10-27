# from lexer import lexer
# from parse import Parser
# from interpreter import Interpreter

# test_code = """kwa kila i katika 1 hadi 5 fanya
#                     chapisha i
#                 mwisho"""

# test_tokens = lexer(test_code)
# print("Tokens:")
# print(test_tokens)

# parser = Parser(test_tokens)
# ast = parser.parse_program()
# print("AST:")
# print(ast)

# interpreter = Interpreter()
# res = interpreter.interpret_program(ast)
# print("Result:")
# print(res)

# test_swascript.py

import argparse
from lexer import lexer
from parse import Parser
from interpreter import Interpreter


def main():
    argparser = argparse.ArgumentParser(
        description="SwahiliScript Interpreter")
    argparser.add_argument("filename", help="Path to the .swa file to execute")
    args = argparser.parse_args()

    # Read the SwahiliScript code from the specified file
    with open(args.filename, "r") as file:
        swa_code = file.read()

    # Tokenize the code
    tokens = lexer(swa_code)

    # Parse the tokens into an AST
    parser = Parser(tokens)
    ast = parser.parse_program()

    # Interpret the AST
    interpreter = Interpreter()
    res = interpreter.interpret_program(ast)

    # Print the result
    print(res)


if __name__ == "__main__":
    main()
