class OperatorPrecedenceParser:
    def __init__(self):
        # Define operator precedence levels
        self.operators = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3
        }

    def parse(self, expression):
        tokens = expression.split()
        output = []
        operator_stack = []

        for token in tokens:
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                # If the token is a number (including negative numbers), add it to the output
                output.append(token)
            elif token in self.operators:
                # If the token is an operator:
                while operator_stack and (self.operators.get(token, 0) <= self.operators.get(operator_stack[-1], 0)):
                    # Pop operators with higher or equal precedence from the stack
                    output.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                # If the token is an opening parenthesis, push it onto the stack
                operator_stack.append(token)
            elif token == ')':
                # If the token is a closing parenthesis:
                while operator_stack and operator_stack[-1] != '(':
                    # Pop operators from the stack and add them to the output until an opening parenthesis is encountered
                    output.append(operator_stack.pop())
                if operator_stack and operator_stack[-1] == '(':
                    operator_stack.pop()  # Pop the opening parenthesis
            else:
                raise ValueError("Invalid token: " + token)

        # Pop any remaining operators from the stack to the output
        while operator_stack:
            output.append(operator_stack.pop())

        # Return the postfix expression as a string
        return ' '.join(output)

    def evaluate(self, postfix_expr):
        stack = []

        for token in postfix_expr.split():
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                # If the token is a number (including negative numbers), push it onto the stack
                stack.append(float(token))
            elif token in self.operators:
                if len(stack) < 2:
                    raise ValueError("Not enough operands for operator: " + token)

                # If the token is an operator, perform the corresponding operation
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == '+':
                    res = operand1 + operand2
                elif token == '-':
                    res = operand1 - operand2
                elif token == '*':
                    res = operand1 * operand2
                elif token == '/':
                    if operand2 == 0:
                        raise ValueError("Division by zero")
                    res = operand1 / operand2
                elif token == '^':
                    res = operand1 ** operand2
                stack.append(res)
            else:
                raise ValueError("Invalid token: " + token)

        if len(stack) != 1:
            raise ValueError("Invalid expression")

        # The result should be the only value left in the stack
        return stack[0]


if __name__ == "__main__":
    parser = OperatorPrecedenceParser()
    expression = "-3 + 4 / 2 / ( 1 - 5 ) ^ 3"

    try:
        # Convert the infix expression to postfix notation
        postfix_expression = parser.parse(expression)

        # Evaluate the postfix expression and print the result
        result = parser.evaluate(postfix_expression)

        print("Postfix Expression:", postfix_expression)
        print("Result:", result)
    except ValueError as e:
        print("We Mzee:", e)






#   NOW, WHAT IN THE WORLD😱 IS A POSTFIX EXPRESSION? You might WONDER🤔.

#   A postfix expression, also known as Reverse Polish Notation (RPN), is a mathematical notation
#   where operators come after their operands. This notation eliminates the need for parentheses
#   to specify the order of operations.
#
#   FOR EXAMPLE:
#   The infix expression "3 + 4" would be written in postfix notation as "3 4 +".
#   Similarly, "5 * (2 + 8)" in infix notation becomes "5 2 8 + * " in postfix notation.
#
#   One of the main advantages of postfix notation is that it eliminates the need for parentheses to indicate the order of operations.🙃

#   Good, now we know something new😁🤸🏾
