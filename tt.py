import random
import itertools

N = 10
time_points = [random.randrange(0, 1000) for i in range(N)]
segments = [(tp, random.randrange(tp, 1000)) for tp in time_points]

events = [[(st, 1), (end, -1)] for (st, end) in segments]
events = list(itertools.chain.from_iterable((events)))
events = sorted(events, key=lambda x: x[0])

print(segments)
print(events)

mmax, cur = 0, 0

for _, event in events:
    cur += event
    mmax = max(mmax, cur)

print(mmax)