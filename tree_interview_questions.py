"""
1. Given the root to a binary tree, count the total number of nodes there are.

2. Given the root to a binary tree, return the deepest node.
"""

from typing import Optional, Tuple, Union, cast
from dataclasses import dataclass


@dataclass(frozen=False)
class Node:
    val: str
    left: Optional["Node"] = None
    right: Optional["Node"] = None

    @property
    def count(self):
        left = self.left.count if self.left else 0
        right = self.right.count if self.right else 0
        return 1 + left + right


def inc_depth(node_depth: Tuple[Optional[Node], int]):
    node, depth = node_depth
    return (node, depth + 1)


def deepest(node: Optional[Node],
            parent: Optional[Node]) -> Tuple[Optional[Node], int]:
    if not node:
        return (parent, 0)

    return inc_depth(
        max(deepest(node.left, node),
            deepest(node.right, node),
            key=lambda x: x[1]))


def check(actual: Union[Node, int], expected: Union[Node, int]):
    assert actual == expected, f"{expected} expected, but got {actual}."
    print("ok")


def solution1(node: Node) -> int:
    return node.count


def solution2(node: Node) -> Node:
    return cast(Node, deepest(node, None)[0])


if __name__ == "__main__":
    leaf = Node("right.right.right")
    root1 = Node(
        "root", Node("left", Node("left.left")),
        Node("right", Node("right.left"), Node("right.right", None, leaf)))
    check(solution1(root1), 7)
    check(solution2(root1), leaf)
