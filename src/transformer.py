from lark import Transformer, Token
from src.models import Condition, AndCondition, OrCondition


class QueryTransformer(Transformer):
    def start(self, items):
        return items[0]

    def condition(self, items):
        field, op, value = items

        field = str(field)
        op = str(op)

        if isinstance(value, Token):
            if value.type == "NUMBER":
                value = float(value)
            elif value.type == "ESCAPED_STRING":
                value = value.value.strip('"')
            elif value.type == "SINGLE_STRING":
                value = value.value.strip("'")

        return Condition(field=field, op=op, value=value)

    def and_op(self, items):
        return AndCondition(AND=items)

    def or_op(self, items):
        return OrCondition(OR=items)

    def number(self, n):
        return float(n[0])

    def add(self, items):
        return items[0] + items[1]

    def sub(self, items):
        return items[0] - items[1]

    def mul(self, items):
        return items[0] * items[1]

    def div(self, items):
        return items[0] / items[1]

    def string(self, s):
        return s[0].value.strip('"')

    def single_string(self, s):
        return s[0].value.strip("'")

    def like_condition(self, items):
        field, _, value = items
        return {"field": str(field), "op": "LIKE", "value": value}

    # BETWEEN
    def between_condition(self, items):
        field, _, v1, _, v2 = items
        return {"field": str(field), "op": "BETWEEN", "value": [v1, v2]}
