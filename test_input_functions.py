from input_functions import yes_or_no


def test_yes_or_no():
    assert yes_or_no('да')
    assert not yes_or_no('нет')
    assert yes_or_no('lf')
    assert not yes_or_no('ytn')
    assert yes_or_no('y')
    assert not yes_or_no('n')
    assert yes_or_no('yes')
    assert not yes_or_no('no')
