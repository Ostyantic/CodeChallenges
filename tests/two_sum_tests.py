from code_challenges.two_sum import two_sum


def test_two_sum_exists():
    two_sum([1, 2, 3], 3)


def test_empty_list():
    empty_list = []
    actual = two_sum(empty_list, 8)
    expected = "empty list"
    assert actual == expected


def test_target_8():
    nums = [1, 3, 5]
    target = 8

    actual = two_sum(nums, target)
    expected = [1, 2]

    assert expected == actual


def test_target_6():
    nums = [1, 3, 4, 3, 5]
    target = 6

    actual = two_sum(nums, target)
    expected = [0, 4]

    assert expected == actual


def test_target_74():
    nums = [40, 100, 68, 34]
    target = 74

    actual = two_sum(nums, target)
    expected = [0, 3]

    assert expected == actual