from fuel import convert, gauge

def test_convert_valid_fraction():
    assert convert("5/10") == 50
    assert convert("1/4") == 25
    assert convert("3/5") == 60
    assert convert("50/100") == 50
    assert convert("1/100") == 1
    assert convert("99/100") == 99

def test_convert_invalid_franction():
    try:
        convert("5/0")
        return False
    except ZeroDivisionError:
        pass

    try:
        convert("10/5")
        assert False
    except ValueError:
        pass

    try:
        convert("-1/10")
        assert False
    except ValueError:
        pass

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(-1) == "E"
    assert gauge(101) == "F"