from currency import convert


def test_convert():
    a = '$100.00'
    b = convert(a, '€')
    assert a != b
    assert b == '€100.00'
