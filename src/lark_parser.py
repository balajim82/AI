from lark import Lark

grammar = """
start: or_expr

?or_expr: and_expr
        | or_expr "OR" and_expr   -> or_op

?and_expr: condition
         | and_expr "AND" condition -> and_op

condition: NAME OP expr

# Expression handling
?expr: term
     | expr "+" term   -> add
     | expr "-" term   -> sub

?term: factor
     | term "*" factor -> mul
     | term "/" factor -> div

?factor: NUMBER        -> number
       | ESCAPED_STRING -> string
       | SINGLE_STRING  -> string
       | NAME           -> var
       | "(" expr ")"

OP: ">" | "<" | ">=" | "<=" | "="
NAME: /[a-zA-Z_]+/
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
