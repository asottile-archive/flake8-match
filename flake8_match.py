from __future__ import annotations

import ast
from typing import Any
from typing import Generator

MSG = 'MAT001 do not use match statements'


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.match_statements: list[tuple[int, int]] = []

    def visit_Match(self, node: ast.stmt) -> None:  # TODO: ast.Match
        self.match_statements.append((node.lineno, node.col_offset))
        self.generic_visit(node)


class Plugin:
    def __init__(self, tree: ast.AST):
        self._tree = tree

    def run(self) -> Generator[tuple[int, int, str, type[Any]], None, None]:
        visitor = Visitor()
        visitor.visit(self._tree)

        for line, col in visitor.match_statements:
            yield line, col, MSG, type(self)
