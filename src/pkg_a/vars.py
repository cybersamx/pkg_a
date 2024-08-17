import math

from pkg_c.stats import (
    mean,
    count,
)


def stddev(sample: list[float]) -> float:
    tot = 0.0
    avg = mean(sample)

    for v in sample:
        tot += math.pow(v - avg, 2)

    return math.sqrt(tot/count(sample))
