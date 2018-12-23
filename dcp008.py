"""
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
 """
 
class Node(object):
  def __init__(self, val: int, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
  

def count_unival(root: Node) -> int:
  def __count(root) -> (int, bool):
    if not root.left and not root.right:
      return 1, True
    
    if root.left and not root.right:
      l_count, is_uni = __count(root.left)
      if not is_uni:
        return l_count, False
      else:
        is_uni &= root.val == root.left.val
        return (1 if is_uni else 0) + l_count, is_uni
    
    if not root.left and root.right:
      r_count, is_uni = __count(root.right)
      if not is_uni:
        return r_count, False
      else:
        is_uni &= root.val == root.right.val
        return (1 if is_uni else 0) + r_count, is_uni
    
    l_count, l_is_uni = __count(root.left)
    r_count, r_is_uni = __count(root.right)
    if l_is_uni and r_is_uni and root.val == root.left.val and root.val == root.right.val:
      return 1 + l_count + r_count, True
    return l_count + r_count, False
    
  return __count(root)[0] 



def check(actual, expected):
  assert actual == expected, "{} expected, but got {}".format(expected, actual)
  print("OK")

if __name__ == "__main__":
  check(count_unival(Node(0)), 1)
  check(count_unival(Node(1)), 1)

  check(count_unival(Node(1, Node(0))), 1)
  check(count_unival(Node(1, Node(1))), 2)

  root = Node(0,
    Node(1), Node(0,
      Node(1, Node(1), Node(1)), Node(0)))
  check(count_unival(root), 5)
