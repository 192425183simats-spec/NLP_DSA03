import re

def parse_expression(expression):
    pattern = r'(\w+)\((\w+)\)'
    match = re.fullmatch(pattern, expression.strip())

    if match:
        predicate = match.group(1)
        argument = match.group(2)

        print("Predicate:", predicate)
        print("Argument:", argument)
        print("Valid FOPC Expression")
    else:
        print("Invalid FOPC Expression")

expression = "Human(Ram)"

parse_expression(expression)
