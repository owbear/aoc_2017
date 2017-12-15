
def calc_03a(data):
    assert False, f"Failed on input {data}!"


def test_03a():
    """
    """
    tests = [
    ]

    for data, expected in tests:
        assert result == expected, f"calc_03a({data}): Expected {expected} but got {result}"


def calc_03b(data):
    assert False, f"Failed on input {data}!"


def test_03b():
    """
    """
    tests = [
    ]
    for data, expected in tests:
        result = calc_03b(data)
        assert result == expected, f"calc_03b({data}): Expected {expected} but got {result}"


puzzle_input_03 = 'aa bb cc'
test_03a()
print("04a: %d" % sum(1 for x in puzzle_input_03.split(' ')) if calc_03a(x))
# test_03b()
# print("04b: %d" % calc_03b(puzzle_input_03))
