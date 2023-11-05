class Interpreter:
    def __init__(self):
        self.variables = {}  # Dictionary to store variables

    def interpret(self, ast):
        if ast is not None:
            node_type = ast[0]

            if node_type == "assignment":
                self.assign_variable(ast)
            elif node_type == "identifier":
                return self.get_variable(ast)
            elif node_type == "operator":
                return self.evaluate_expression(ast)
            elif node_type == "if":
                return self.evaluate_if_statement(ast)
            elif node_type == "comparison":
                return self.evaluate_comparison(ast)
            elif node_type == "forloop":
                return self.evaluate_loop(ast)
            elif node_type in ["number", "string", "bool"]:  # is constant
                return ast[1]
            elif node_type == "print":
                return self.interpret(ast[1])
            else:
                raise RuntimeError(f"Invalid AST node: {node_type}")

    def assign_variable(self, ast):
        variable_name = ast[1]
        value = self.interpret(ast[2])
        self.variables[variable_name] = value

    def get_variable(self, ast):
        variable_name = ast[1]
        if variable_name in self.variables:
            return self.variables[variable_name]
        else:
            raise NameError(f"Variable '{variable_name}' is not defined.")

    def evaluate_expression(self, ast):
        operator = ast[1]
        left = self.interpret(ast[2])
        right = self.interpret(ast[3])

        if operator == "+":
            return left + right
        elif operator == "-":
            return left - right
        elif operator == "*":
            return left * right
        elif operator == "/":
            return left / right
        else:
            raise RuntimeError(f"Invalid operator: {operator}")

    def evaluate_if_statement(self, ast):
        condition = self.interpret(ast[1])
        if condition:
            return self.interpret_program(ast[2])
        else:
            return None

    def evaluate_comparison(self, ast):
        operator = ast[1]
        left = self.interpret(ast[2])
        right = self.interpret(ast[3])

        if operator == "ni sawa na":
            return left == right
        elif operator == "si sawa na":
            return left != right
        elif operator == "kubwa kuliko":
            return left > right
        elif operator == "ndogo kuliko":
            return left < right
        elif operator == "kubwasawana":
            return left >= right
        elif operator == "ndogosawana":
            return left <= right
        else:
            raise RuntimeError(f"Invalid operator: {operator}")

    def evaluate_loop(self, ast):
        variable_name = ast[1]
        start = int(self.interpret(ast[2][0]))
        end = int(self.interpret(ast[2][1]))

        body = ast[3]

        # initialize array of None values for output
        result = [None] * (end - start + 1)

        for i in range(start, end + 1):
            self.variables[variable_name] = i
            result[i - start] = self.interpret_program(body)

        return result

    def interpret_program(self, program):
        result = None
        for statement in program:
            result = self.interpret(statement)
        return result
