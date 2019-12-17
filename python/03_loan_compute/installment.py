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
    mr = searchBelta(r, r * 3, 1 - m / n, r + 1 / n, m)
    return mr, (1 + mr) ** 12 - 1

for m in range(2, 61):
    mr, yr = getBelta(60, m, 0.0025)
    print('%02d期' % m, '%.3f%%' % (mr * 100), '%.3f%%' % (mr * 1200), '%.3f%%' % (yr * 100))
