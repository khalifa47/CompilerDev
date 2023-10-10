def is_comment(line): # checks if line is regular comment
    return line.strip().startswith("#")

def identify_comments(filepath):
    # Reads file in given path
    with open(filepath, "r") as f:
        lines = f.readlines()

    # identifies each line as either a comment or not and adds it to a result as (line_number, is_comment)
    res = []
    for i, line in enumerate(lines):
        res.append((i+1, is_comment(line)))

    return res

print(identify_comments("test.py"))

# Example Output:
# [(1, True), (2, False), (3, False), (4, False), (5, True), (6, False), (7, False), (8, False), (9, True)]

# PS: Responses to the questions in the readme.md in this folder.
