import itertools


def generate_walk():
    directions = itertools.cycle([(1, 0), (0, -1), (-1, 0), (0, 1)])
    i, j = 0, 0
    n = 1
    run = 1
    while True:
        for x in range(2):
            direction = next(directions)
            for s in range(run):
                i += direction[0]
                j += direction[1]
                n += 1
                yield n, i, j
        run += 1


def calc_03a(data):
    if data == 1:
        return 0
    walk = generate_walk()
    for n, i, j in walk:
        if n == data:
            return abs(i) + abs(j)
    assert False, f"{data} was not found!"


def test_03a():
    """
    Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up
    while spiraling outward. For example, the first few squares are allocated like this:

    17  16  15  14  13
    18   5   4   3  12
    19   6   1   2  11
    20   7   8   9  10
    21  22  23---> ...
    While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1
    (the location of the only access port for this memory system) by programs that can only move up, down, left, or right.
    They always take the shortest path: the Manhattan Distance between the location of the data and square 1.

    For example:

    Data from square 1 is carried 0 steps, since it's at the access port.
    Data from square 12 is carried 3 steps, such as: down, left, left.
    Data from square 23 is carried only 2 steps: up twice.
    Data from square 1024 must be carried 31 steps.
    """
    tests = [
        (1, 0),
        (12, 3),
        (23, 2),
        (1024, 31)
    ]

    for data, expected in tests:
        result = calc_03a(data)
        assert result == expected, f"calc_03a({data}): Expected {expected} but got {result}"


def sum_neighbours(values, i, j):
    offsets = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0),           (1, 0),
        (-1, 1), (0, 1), (1, 1)
    ]
    return sum([values.get((i + n, j + m), 0) for n, m in offsets])


def calc_03b(data):
    if data == 1:
        return 2
    values = {(0, 0): 1}
    walk = generate_walk()
    for n, i, j in walk:
        neighbours = sum_neighbours(values, i, j)
        if neighbours > data:
            return neighbours
        values[(i, j)] = neighbours
    assert False, f"Failed on input {data}!"


def test_03b():
    """
    So, the first few squares' values are chosen as follows:

    Square 1 starts with the value 1.
    Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
    Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
    Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
    Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.
    Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:

    147  142  133  122   59
    304    5    4    2   57
    330   10    1    1   54
    351   11   23   25   26
    362  747  806--->   ...
    What is the first value written that is larger than your puzzle input?
    """
    tests = [
        (1, 2),
        (2, 4),
        (4, 5),
        (5, 10),
        (10, 11),
        (11, 23)
    ]
    for data, expected in tests:
        result = calc_03b(data)
        assert result == expected, f"calc_03b({data}): Expected {expected} but got {result}"


puzzle_input_03 = 347991
test_03a()
print("03a: %d" % calc_03a(puzzle_input_03))
test_03b()
print("03b: %d" % calc_03b(puzzle_input_03))
