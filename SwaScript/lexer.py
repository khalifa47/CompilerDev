import re

TOKEN_TYPES = [
    ("BOOL", r"kweli|uwongo"),
    ("OPERATOR", r"\+|-|\*|/"),
    ("COMPARISON", r"ni sawa na|si sawa na|kubwa kuliko|ndogo kuliko|kubwasawana|ndogosawana"),
    ("KEYWORD", r"kuwa|chapisha|weka|ikiwa|basi|mwisho|kwa kila|katika|hadi|fanya|funza"),
    ("STRING", r'"[^"]*"'),
    ("IDENTIFIER", r"[A-Za-z]+"),
    ("NUMBER", r"\d+(\.\d+)?"),
    ("PUNCTUATION", r"\(|\)"),
    ("NEWLINE", r"\n"),
    ("WHITESPACE", r"\s+"),
]


def lexer(code):
    tokens = []
    line_number = 1

    while code:
        for token_type, pattern in TOKEN_TYPES:
            match = re.match(pattern, code)
            if match:
                value = match.group(0)
                if token_type == "NEWLINE":
                    line_number += 1
                elif token_type != "WHITESPACE":
                    tokens.append((token_type, value, line_number))
                code = code[len(value):]
                break
        else:
            raise SyntaxError(
                f"Invalid syntax at line {line_number}: {code[:10]}...")

    # Add an end-of-file token for convenience
    tokens.append(("EOF", "", line_number))

    return tokens
