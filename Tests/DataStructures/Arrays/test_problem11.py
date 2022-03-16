from DataStructures.Arrays import problem11


def test_empty():
    foo = problem11
    elements = []
    result = []

    assert foo.solve(elements) == result


def test_calculation():
    foo = problem11
    elements = [1, 2, 3, 4, 5]
    result = [120, 60, 40, 30, 24]

    assert foo.solve(elements) == result

# 3,6,6
# 6,2,1
# 2, 3, 6
def test_other_calculation():
    foo = problem11
    elements = [3, 2, 1]
    result = [2, 3, 6]

    assert foo.solve(elements) == result
