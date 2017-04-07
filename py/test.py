import numpy as np



def sumx(x, power):
    if len(x) > 0:
        y = x ** 10
        print(y)
        return np.sum((1.0 / x) ** power)
    else:
        return 0


if __name__ == '__main__':
    x = np.array([1, 2, 3, 5, 6, 7, 8, 9])
    print(sumx(x, 200))
    print(sumx(x, 2))

    print(sumx(np.array([]), 1))
    print(type(sumx([4], 2)))

