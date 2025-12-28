from euler.solutions.p17 import to_word


def test_thousands():
    assert to_word(1000) == "onethousand"


def test_hundreds():
    assert to_word(900) == "ninehundred"
    assert to_word(100) == "onehundred"


def test_hundreds_with_remainder():
    assert to_word(342) == "threehundredandfortytwo"
    assert to_word(115) == "onehundredandfifteen"


def test_tens():
    assert to_word(40) == "forty"
    assert to_word(99) == "ninetynine"


def test_teens():
    assert to_word(13) == "thirteen"
    assert to_word(19) == "nineteen"


def test_euler_example():
    total_chars = 0
    for i in range(1, 5 + 1):
        word = to_word(i)
        total_chars += len(word)
    assert total_chars == 19  # one + two + three + four + five =
