# coding: utf-8

def prod(inp):
    output = []
    right = 1
    for number in reversed(inp):
        output.insert(0, right)
        right *= number
    left = 1
    for i, number in enumerate(inp):
        output[i] *= left
        left *= number
    return output


def main():
    inp = [1, 2, 3, 4, 5]
    out = prod(inp)
    print(out)

main()
