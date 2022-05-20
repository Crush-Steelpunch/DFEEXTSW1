import leonsfuncs

def test_animaltesting():
    assert leonsfuncs.animaltesting("cat") == False

def test_animaltesting2():
    assert leonsfuncs.animaltesting("dog") == True

def test_animaltesting3():
    assert leonsfuncs.animaltesting("feline") == False

def test_add1_1():
    assert leonsfuncs.add1(1) == 2

def test_sorted():
    assert leonsfuncs.sorted() == "Leon is sorted, nice one!"