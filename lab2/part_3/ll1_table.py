from collections import OrderedDict
from tabulate import tabulate

# Define special symbols
EMPTY = "ε"
END = "$"

# CFG here
grammar_str = """
    E -> T E'
    E' -> + T E' | ε
    T -> F T'
    T' -> * F T' | ε
    F -> ( E ) | id
"""


# Parse the grammar string and convert it into a dictionary
def parse_grammar(grammar):
    G = OrderedDict()

    for production in grammar.strip().split("\n"):
        left, right = production.split("->")
        left = left.strip()
        right = [rule.strip().split() for rule in right.strip().split("|")]
        G[left] = right

    return G


# Compute the FIRST set for a given grammar
def compute_first_set(grammar):
    first = dict()

    def add(k, v):
        m = first.get(k, set())
        m.add(v)
        first[k] = m

    def calculate_first(non_terminal):
        result = []

        for production in grammar[non_terminal]:
            for symbol in production:
                if isinstance(symbol, str):
                    add(non_terminal, symbol)
                    result.insert(0, symbol)
                    if symbol == EMPTY:
                        add(non_terminal, symbol)
                    else:
                        break
                else:
                    Z = calculate_first(symbol)
                    for x in {
                        Z[i] for i in range(Z.index(EMPTY) if EMPTY in Z else len(Z))
                    }:
                        result.insert(0, x)
                        add(non_terminal, x)

        for n in result:
            add(non_terminal, n)
        return result

    for non_terminal in grammar:
        calculate_first(non_terminal)

    return first


# Generate the LL(1) parsing table
def generate_parsing_table(grammar, first):
    parsing_table = dict()

    def add_entry(non_terminal, terminal, production):
        if non_terminal not in parsing_table:
            parsing_table[non_terminal] = {}
        if terminal in parsing_table[non_terminal]:
            raise ValueError(
                f"Grammar is not LL(1) due to multiple entries for ({non_terminal}, {terminal})."
            )
        parsing_table[non_terminal][terminal] = production

    for non_terminal in grammar:
        for production in grammar[non_terminal]:
            first_set = compute_first_for_production(production, first)
            for terminal in first_set:
                if terminal != EMPTY:
                    add_entry(non_terminal, terminal, production)

            if EMPTY in first_set:
                follow_set = compute_follow_set(non_terminal, grammar, first)
                for terminal in follow_set:
                    add_entry(non_terminal, terminal, production)

    return parsing_table


# Compute the FIRST set for a production (sequence of symbols)
def compute_first_for_production(production, first):
    first_set = set()
    for symbol in production:
        if symbol in first:
            first_set.update(first[symbol])
            if EMPTY not in first[symbol]:
                break
        else:
            first_set.add(symbol)
            break
    return first_set


# Compute the FOLLOW set for a non-terminal
def compute_follow_set(non_terminal, grammar, first):
    follow_set = set()

    if non_terminal == "S":
        follow_set.add(END)

    for symbol, productions in grammar.items():
        for production in productions:
            for i, p_symbol in enumerate(production):
                if p_symbol == non_terminal:
                    remaining_symbols = production[i + 1 :]
                    first_set = compute_first_for_production(remaining_symbols, first)
                    follow_set.update(first_set)
                    if EMPTY in first_set:
                        follow_set.update(compute_follow_set(symbol, grammar, first))

    return follow_set


# Print the LL(1) parsing table in a tabular format
def print_table(parsing_table):
    headers = list(parsing_table.keys())
    headers.insert(0, "Terminals")
    table = []
    for terminal in set(
        terminal
        for non_terminal in parsing_table
        for terminal in parsing_table[non_terminal]
    ):
        row = [terminal]
        for non_terminal in parsing_table:
            if terminal in parsing_table[non_terminal]:
                row.append(f"{non_terminal} → {parsing_table[non_terminal][terminal]}")
            else:
                row.append("")
        table.append(row)

    print(tabulate(table, headers, tablefmt="fancy_grid"))


if __name__ == "__main__":
    # Parse the grammar string
    grammar = parse_grammar(grammar_str)

    # Compute the FIRST set
    first = compute_first_set(grammar)

    # Generate the LL(1) parsing table
    parsing_table = generate_parsing_table(grammar, first)

    # Print the LL(1) parsing table
    print("LL(1) Parsing Table:")
    print_table(parsing_table)
