from src.lark_parser import parser
from src.transformer import QueryTransformer

transformer = QueryTransformer()


class QueryService:

    def parse(self, query: str):
        try:
            tree = parser.parse(query)
            print(f"Parse tree: {transformer.transform(tree)}")
            return transformer.transform(tree)
        except Exception as e:
            print(f"Error QueryService service: {e}")
            raise ValueError(f"Invalid query: {e}")
