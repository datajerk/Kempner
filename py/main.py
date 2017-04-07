# compute binomial coefficients
import itertools
import numpy as np
from scipy.special import binom


def rec(k, w, m):
    def power(a, b):
        if a == 0 and b == 0:
            return 1
        else:
            return a ** b

    def c(k, w):
        return ((-1) ** w) * binom(k + w - 1, w)

    return 10**(-k - w) * c(k, w) * power(m, w)


def sumx(x, power):
    if len(x) > 0:
        return np.sum((1 / x) ** power)
    else:
        return 0


if __name__ == '__main__':
    S = 42
    digits = {i: int(ch) for i, ch in enumerate(str(S))}
    T = np.ones((len(digits), 10))

    T[0, digits[0]] = 2
    T[1, digits[0]] = 2

    T[1, digits[1]] = 0

    n = T.shape[0]
    f = np.full((n, n, 10), 0)

    # given T compute f, see equation (4)
    # note that arrays start with index 0...
    i, j = np.nonzero(T)
    for (a, b) in zip(i, j):
        f[int(T[a, b]) - 1, a, b] = 1

    # loop over slices of f to compute A, see equation (7)
    A = np.sum(f[:, :, s] / 10 for s in range(f.shape[-1]))
    I = np.identity(n=A.shape[0])

    B = np.linalg.inv(I - A) - I

    # define the sets S_1, ..., S_n explicitly for up to 5 digits
    m = 5
    S = np.empty((m, T.shape[0]), dtype=object)

    for j in range(0, S.shape[1]):
        S[0, j] = np.where(T[0, 1:] == j + 1)[0] + 1

    # loop over d digit sets...
    for digit in range(1, S.shape[0]):
        # note that in S[1] are the 2-digit numbers, S[2] are 3-digit numbers
        # to those sets append m, typcially m=0...9
        for b in range(0, S.shape[1]):
            S[digit, b] = np.array([])

        for m in range(0, f.shape[-1]):
            # f describes the transistion from set S[digit-1,l] to S[digit,j]
            j, l = np.nonzero(f[:, :, m])
            for (a, b) in zip(j, l):
                S[digit, a] = np.append(S[digit, a], 10 * S[digit - 1, b] + m)

    psi = np.zeros((50, S.shape[1], 30))

    # for small numbers, e.g. up to 5 digits
    for (i, j), value in np.ndenumerate(S):
        for k in range(1, 30):
            psi[i, j, k] = sumx(value, power=k)

    for (i, j) in itertools.product(range(S.shape[0], psi.shape[0]), range(0, S.shape[1])):
        for k in range(1, 30):
            a = 0
            for (l, m), value in np.ndenumerate(f[j, :, :]):
                inner = np.sum([rec(k, w, m) * psi[i - 1, l, k + w] for w in range(0, 30 - k)])
                a += value * inner

            psi[i, j, k] = a
            if a < 1e-20:
                break

    vec = psi[psi.shape[0] - 1, :, 1]
    print(np.sum(np.sum(psi[:, :, 1])) + np.sum(np.dot(B, vec)))
