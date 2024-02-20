from code_challenges.two_sum import two_sum


def test_two_sum_exists():
    numbers = [1, 3, 5]
    actual = two_sum(numbers, 8)
    assert actual

def test_empty_list():
    empty_list = []
    actual = two_sum(empty_list, 8)
    expected = "empty list"
    assert actual == expected
