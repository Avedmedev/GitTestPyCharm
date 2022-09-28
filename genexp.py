import time


def gen():
    print("Gen func")
    time.sleep(3)
    return 1, 2, 3


if __name__ == '__main__':
    g = (el for el in gen())
    print(next(g))
    print(next(g))
    print(next(g))
