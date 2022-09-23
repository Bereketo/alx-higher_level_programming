#!/usr/bin/python3
if __name__ == '__main__':
    """print sum of arguments."""
    from sys import argv
    add = 0
    leng = len(argv)
    if (leng == 1):
        print(0)
    for i in range(1, leng):
        add = add + int(argv[i])
    print(add)
