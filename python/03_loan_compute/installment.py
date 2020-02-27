import numpy as np
import matplotlib.pyplot as plt

def getError(b, s, t, m):
    a = (1 + b) ** m
    return (a - s) * (b - t) - t * (s - 1)

def searchBelta(b1, b2, s, t, m):
    assert b1 < b2
    b = (b1 + b2) / 2
    if (b2 - b1 < 10e-6):
        return b
    e1 = getError(b1, s, t, m)
    e2 = getError(b2, s, t, m)
    assert e1 * e2 < 0
    e = getError(b, s, t, m)
    if (0 == e):
        return b
    if (e1 * e < 0):
        return searchBelta(b1, b, s, t, m)
    else:
        return searchBelta(b, b2, s, t, m)

def getBelta(n, m, r):
    # n: 分期数
    # m: 提前还款期数
    # r: 分期手续费
    # b: 实际利率
    # (1+b)^m-(1/n+r)((1+b)^m-1)/b=1-m/n
    if (m <= 1):
        return 0
    else:
        return searchBelta(r, r * 3, 1 - m / n, r + 1 / n, m)

m = [x for x in range(2, 61)]
mr = [getBelta(60, x, 0.0025) for x in m]
yr1 = [x * 1200 for x in mr]
yr2 = [((1 + x) ** 12 - 1) * 100 for x in mr]

for i in m:
    print('%02d期' % i, '%.3f%%' % (100 * mr[i - 2]), '%.3f%%' % yr1[i - 2], '%.3f%%' % yr2[i - 2])

x = np.array(m)
y0 = np.ones(len(m)) * 4.9
y1 = np.array(yr1)
y2 = np.array(yr2)
plt.plot(x, y0, color="green", linewidth=1)
plt.plot(x, y1, color="blue", linewidth=1)
plt.plot(x, y2, color="red", linewidth=1)
plt.show()
