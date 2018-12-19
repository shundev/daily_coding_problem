# coding: utf-8
# Your code here!

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    

def serialize(root: Node) -> str:
    values = []
    def helper(node: Node):
        if not node:
            values.append("?")
            return
        
        values.append(node.value)
        helper(node.left)
        helper(node.right)
        return
    
    helper(root)
    return "/".join(values)


def deserialize(s: str) -> Node:
    values = iter(s.split("/"))
    def helper() -> Node:
        val = next(values)
        if val == "?":
            return None
        
        return Node(val, helper(), helper())
        
    return helper()


if __name__ == "__main__":
    node = Node("root", Node("left", Node("left.left")), Node("right"))
    s1 = serialize(node)
    s2 = serialize(deserialize(s1))
    print(s1)
    print(s2)
    assert s1 == s2
