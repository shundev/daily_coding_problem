from typing import List
"""
This problem was asked by Google.

Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2.
subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1.
subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system.
For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext",
and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format,
return the length of the longest absolute path to a file in the abstracted file system.
If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.
"""


def longest_path(s: str) -> int:
    splited = s.split("\n")
    longest: int = 0
    for i in range(len(splited)):
        if "." not in splited[i]:
            continue

        path_to_file: List[str] = []
        for j in range(0, i + 1):
            level = splited[j].count("\t")
            if level >= len(path_to_file):
                path_to_file.append(splited[j].strip())
            else:
                path_to_file[level] = splited[j].strip()

        length: int = 0
        length = len("/".join(path_to_file))
        if length > longest:
            longest = length
    return longest


def check(actual: int, expected: int):
    assert actual == expected, f"{expected} expected, but got {actual}."
    print("ok")


if __name__ == "__main__":
    s1 = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    l1 = 20
    s2 = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    l2 = 32
    check(longest_path(s1), l1)
    check(longest_path(s2), l2)
