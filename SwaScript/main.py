import argparse
from lexer import lexer
from parse import Parser
from interpreter import Interpreter
from pprint import pprint


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
    print("\n====================================TOKENS====================================\n")
    pprint(tokens)
    print("\n==============================================================================\n")

    # Parse the tokens into an AST
    parser = Parser(tokens)
    ast = parser.parse_program()
    print("\n=====================================AST======================================\n")
    pprint(ast)
    print("\n==============================================================================\n")

    # Interpret the AST
    interpreter = Interpreter()
    res = interpreter.interpret_program(ast)

    # Print the result
    print("\n====================================RESULT====================================\n")
    pprint(res)
    print("\n==============================================================================\n")


if __name__ == "__main__":
    main()
