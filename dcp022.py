"""
This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces),
return the original sentence in a list.
If there is more than one possible reconstruction, return any of them.
If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and
the string "thequickbrownfox",
you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and
the string "bedbathandbeyond",
return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""

from typing import List


def solution(ss: str, dic: List[str]) -> List[str]:
    if not dic:
        return []
    ret: List[str] = []
    buf: str = ""
    for i in range(len(ss)):
        buf += ss[i]
        for word in dic:
            if buf == word:
                ret.append(word)
                buf = ""

    return ret


def check(actual: List[str], expected: List[List[str]]):
    if not actual and not expected:
        print("ok")
        return

    if actual and expected:
        assert actual in expected, f"Any of {expected} expected, but got {actual}."
        print("ok")
        return

    assert False, f"{expected} expected, but got {actual}."


if __name__ == "__main__":
    s1 = "thequickbrownfox"
    dic1 = ['quick', 'brown', 'the', 'fox']
    ans1 = [['the', 'quick', 'brown', 'fox']]

    s2 = "bedbathandbeyond"
    dic2 = ['bed', 'bath', 'bedbath', 'and', 'beyond']
    ans2 = [['bed', 'bath', 'and', 'beyond'], ['bedbath', 'and', 'beyond']]

    check(solution("hoge", []), [])
    check(solution(s1, dic1), ans1)
    check(solution(s2, dic2), ans2)
