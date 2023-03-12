#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    num_args = len(args)

    if num_args == 0:
        print("Arguments:")
    elif num_args == 1:
        print("Arguments")
        print("1: {}".format(args[0]))
    else:
        print("{} Arguments:".format(num_args))
        for i in range(num_args):
            print("{}: {}".format(i+1, args[i]))
