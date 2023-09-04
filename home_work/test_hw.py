def test_dz1():
    assert ('home', 'work') == ('home', 'work')


def test_dz2():
    assert 'QA' != 'QC'


def test_dz3():
    assert not (1, 1, 2, 3, 5) == (2, 3, 5)
