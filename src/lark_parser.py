from lark import Lark


grammar = """
start: or_expr

?or_expr: and_expr
        | or_expr "OR" and_expr   -> or_op

?and_expr: condition
         | and_expr "AND" condition -> and_op

condition: NAME OP VALUE

OP: ">" | "<" | ">=" | "<=" | "="
NAME: /[a-zA-Z_]+/
VALUE: NUMBER | ESCAPED_STRING | SINGLE_STRING
SINGLE_STRING: /'[^']*'/

%import common.NUMBER
%import common.ESCAPED_STRING
%import common.WS
%ignore WS
"""
try:
    parser = Lark(grammar, parser="lalr")
except Exception as e:
    print(f"Error creating parser: {e}")
    raise ValueError(f"Failed to create parser: {e}")
