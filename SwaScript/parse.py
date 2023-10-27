class Parser:
    def __init__(self, tokens):
        self.terminator = None
        self.tokens = tokens

    def parse_program(self):
        program = []
        while self.tokens and self.tokens[0][0] != "EOF":
            statement = self.parse_statement()
            if statement:
                program.append(statement)
        return program

    def parse_statement(self):
        token_type, token_value, line_number = self.tokens[0]

        if token_type == "KEYWORD":
            if token_value == "chapisha":
                self.tokens.pop(0)
                expression = self.parse_expression()
                return ("print", expression, line_number)
            elif token_value == "weka":
                self.tokens.pop(0)
                variable_name = self.tokens.pop(0)[1]
                if self.tokens[0][1] == "kuwa":
                    self.tokens.pop(0)  # Consume "kuwa"
                    expression = self.parse_expression()
                    while self.tokens and self.tokens[0][0] == "OPERATOR":
                        operator = self.tokens.pop(0)[1]
                        next_expression = self.parse_expression()
                        expression = ("operator", operator,
                                      expression, next_expression)
                    return ("assignment", variable_name, expression, line_number)
            elif token_value == "mwisho":
                self.terminator = self.tokens.pop(0)[1]  # pop "mwisho"
                return None
            elif token_value == "ikiwa":
                self.tokens.pop(0)
                condition = self.parse_expression()
                while self.tokens and self.tokens[0][0] == "COMPARISON":
                    operator = self.tokens.pop(0)[1]
                    next_condition = self.parse_expression()
                    condition = ("comparison", operator,
                                 condition, next_condition)
                if self.tokens[0][1] == "basi":
                    self.tokens.pop(0)
                    body = self.parse_program()
                    if self.terminator == "mwisho":
                        self.terminator = None
                        return ("if", condition, body, line_number)
                    else:
                        raise SyntaxError(
                            f"Expected 'mwisho' at line {line_number}")
                else:
                    raise SyntaxError(f"Expected 'basi' at line {line_number}")
            elif token_value == "kwa kila":
                self.tokens.pop(0)  # Consume "kwa kila"
                variable_name = self.tokens.pop(0)[1]
                if self.tokens[0][1] == "katika":
                    self.tokens.pop(0)  # Consume "katika"
                    range_start = self.parse_expression()
                    if self.tokens[0][1] == "hadi":
                        self.tokens.pop(0)  # Consume "hadi"
                        range_end = self.parse_expression()
                        if self.tokens[0][1] == "fanya":
                            self.tokens.pop(0)  # Consume "fanya"
                            body = self.parse_program()
                            if self.terminator == "mwisho":
                                self.terminator = None
                                return ("forloop", variable_name, (range_start, range_end), body, line_number)
                            else:
                                raise SyntaxError(
                                    f"Expected 'mwisho' at line {line_number}")
                        else:
                            raise SyntaxError(
                                f"Expected 'fanya' at line {line_number}")
                    else:
                        raise SyntaxError(
                            f"Expected 'hadi' at line {line_number}")
                else:
                    raise SyntaxError(
                        f"Expected 'katika' at line {line_number}")
            # Add parsing for other keywords and statements (function_definition, etc.)
        raise SyntaxError(
            f"Invalid statement: {token_value} at line {line_number}")

    def parse_expression(self):
        token_type, token_value, line_number = self.tokens[0]

        if token_type == "NUMBER":
            self.tokens.pop(0)
            return ("number", float(token_value))
        elif token_type == "STRING":
            self.tokens.pop(0)
            return ("string", token_value[1:-1])
        elif token_type == "BOOL":
            self.tokens.pop(0)
            return ("bool", True if token_value == "kweli" else False)
        elif token_type == "IDENTIFIER":
            self.tokens.pop(0)
            return ("identifier", token_value)
        elif token_type == "TYPE":
            self.tokens.pop(0)
            return ("type", token_value)
        elif token_type == "OPERATOR":
            self.tokens.pop(0)
            left = self.parse_expression()
            right = self.parse_expression()
            return ("operator", token_value, left, right)
        elif token_type == "COMPARISON":
            self.tokens.pop(0)
            left = self.parse_expression()
            right = self.parse_expression()
            return ("comparison", token_value, left, right)
        elif token_type == "PUNCTUATION" and token_value == "(":
            self.tokens.pop(0)
            expression = self.parse_expression()
            if self.tokens[0][1] == ")":
                self.tokens.pop(0)
                return expression
            else:
                raise SyntaxError(f"Expected ')' at line {line_number}")
        elif token_type == "EOF":
            return None
        raise SyntaxError(
            f"Invalid expression: {token_value} at line {line_number}")
