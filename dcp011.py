from typing import Dict, List


class Node:
    def __init__(self, val: str):
        self.val: str = val
        self.lefs: Dict[str, Node] = dict()

    def get_strings(self) -> List[str]:
        ret: List[str] = []
        for c, node in self.lefs.items():
            if len(node.lefs) == 0:
                ret.append(c)
            for s in node.get_strings():
                ret.append(c + s)
        return ret

    def load(self, s: str) -> "Node":
        if s in self.lefs:
            return self.lefs[s]

        n: Node = Node(s)
        self.lefs[s] = n
        return n

    def find(self, s: str) -> "Node":
        return self.lefs[s]


class Tree:
    def __init__(self):
        self.head: Node = Node("^")

    def load(self, s: str):
        n: Node = self.head
        for c in s:
            n = n.load(c)

    def find(self, s: str) -> List[str]:
        n: Node = self.head
        for c in s:
            n = n.find(c)
            if not n:
                return []
        return n.get_strings()


def node_test():
    tree = Tree()
    tree.load("dog")
    tree.load("deer")
    tree.load("deal")
    ans = tree.find("de")
    [print("de" + x) for x in ans]


if __name__ == "__main__":
    node_test()
