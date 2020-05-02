import math

INFINITY = float("inf")


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y

    def __repr__(self) -> str:
        return "({0.x}, {0.y})".format(self)


def cbrt(x: float) -> float:
    return math.pow(x, 1 / 3) if x > 0 else -math.pow(-x, 1 / 3)


def sqrt(x: float) -> float:
    return math.sqrt(x) if x > 0 else 0


def sq(x: float) -> float:
    return x * x


def cb(x: float) -> float:
    return x * x * x


def time(pt1: Point, ct1: Point, ct2: Point, pt2: Point, x: float) -> float:
    a = pt1.x - 3 * ct1.x + 3 * ct2.x - pt2.x
    b = 3 * ct1.x - 6 * ct2.x + 3 * pt2.x
    c = 3 * ct2.x - 3 * pt2.x
    d = pt2.x - x

    if abs(a) < 0.000000001:  # quadratic
        if abs(b) < 0.000000001:  # linear
            return -d / c

        qb = c / b
        qc = d / b
        tmp = sqrt(sq(qb) - 4 * qc)
        return (-qb + (tmp if (qb > 0 or qc < 0) else -tmp)) / 2

    p = -sq(b) / (3 * sq(a)) + c / a
    q = 2 * cb(b / (3 * a)) - b * c / (3 * sq(a)) + d / a
    addcoef = -b / (3 * a)

    lmbd = sq(q) / 4 + cb(p) / 27
    if lmbd >= 0:  # real
        sqlambda = sqrt(lmbd)
        tmp = cbrt(-q / 2 + (sqlambda if q < 0 else -sqlambda))
        return tmp - p / (3 * tmp) + addcoef
    else:
        norm = sqrt(sq(q) / 4 - lmbd)
        if norm < 0.0000000001:
            return addcoef

        angle = math.acos(-q / (2 * norm)) / 3
        fact = 2 * cbrt(norm)
        t = INFINITY
        for i in range(-1, 2):
            tmp = fact * math.cos(angle + i * math.pi * 2 / 3) + addcoef
            if tmp >= -0.000000001 and tmp < t:
                t = tmp

        return t


def value(pt1: Point, ct1: Point, ct2: Point, pt2: Point, x: float) -> float:
    t: float = time(pt1, ct1, ct2, pt2, x)
    return (
        cb(t) * pt1.y
        + 3 * sq(t) * (1 - t) * ct1.y
        + 3 * t * sq(1 - t) * ct2.y
        + cb(1 - t) * pt2.y
    )
