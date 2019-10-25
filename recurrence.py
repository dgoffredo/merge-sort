
import sys


if len(sys.argv) < 2:
    limit = 1000
else:
    limit = int(sys.argv[1])

def complexity_values(up_to):
    # Recurrence is C(n) = n + 2 C(n/2).

    assert up_to >= 0
    memo = [0]

    for i in range(1, up_to + 1):
        memo.append(i + 2 * memo[i // 2])

    return memo


for i, value in enumerate(complexity_values(limit)):
    print(i, value)
