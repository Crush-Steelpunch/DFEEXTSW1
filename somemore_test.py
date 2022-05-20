import leonsfuncs

def test_maxthreenumbers1():
    assert leonsfuncs.maxthreenumbers(2, 3, 4) == 4
def test_maxthreenumbers2():
    assert leonsfuncs.maxthreenumbers(4, 3, 2) == 4
def test_maxthreenumbers3():
    assert leonsfuncs.maxthreenumbers(4, 2, 3) == 4
def test_maxthreenumbers4():
    assert leonsfuncs.maxthreenumbers(3, 2, 4) == 4
def test_maxthreenumbers5():
    assert leonsfuncs.maxthreenumbers(2, 4, 3) == 4