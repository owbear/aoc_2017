import itertools


def calc_steps_06a(data: list):
    seen = {}
    iterations = 0
    while tuple(data) not in seen:
        iterations += 1
        seen[tuple(data)] = iterations

        value = max(data)
        position = data.index(value)
        data[position] = 0

        tail = range(position, len(data))
        head = range(0, position)

        indexes = itertools.cycle(itertools.chain(tail, head))
        next(indexes)
        for n, i in zip(range(value), indexes):
            data[i] += 1
            if n == value:
                break

    return data, iterations, iterations-seen[tuple(data)]+1


def test_06a():
    """
    In each cycle, it finds the memory bank with the most blocks (ties won by the
    lowest-numbered memory bank) and redistributes those blocks among the banks. To
    do this, it removes all of the blocks from the selected bank, then moves to the
    next (by index) memory bank and inserts one of the blocks. It continues doing
    this until it runs out of blocks; if it reaches the last memory bank, it wraps
    around to the first one.
    """
    tests = [
        ([0, 2, 7, 0], [2, 4, 1, 2], 5, 4)
    ]

    for data, expected_banks, expected_steps, expected_length in tests:
        banks, steps, length = calc_steps_06a(data)
        assert expected_banks == banks, f"calc_steps_06a({data}): Expected {expected_banks} but got {banks}"
        assert expected_steps == steps, f"calc_steps_06a({data}): Expected {expected_steps} but got {steps}"
        assert expected_length == length, f"calc_steps_06a({data}): Expected {expected_length} but got {length}"


puzzle_input_06 = [int(x) for x in "2	8	8	5	4	2	3	1	5	5	1	2	15	13	5	14".split()]

test_06a()
print("06a: %s %s %s" % calc_steps_06a(puzzle_input_06.copy()))
