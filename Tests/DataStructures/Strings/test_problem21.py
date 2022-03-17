from DataStructures.Strings import problem21


def test_first_case():
    foo = problem21
    word, string = "ab", "abxaba"
    result = [0, 3, 4]

    assert foo.solve(word, string) == result
