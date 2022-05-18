class letterlist:

    def __init__(self,letterset):
        self.listofletter = letterset

    def lettertest(self, invar):
        if invar.upper() in self.listofletter:
            return True
        else:
            return False

voweltest = letterlist("AEIOU")

romannumeraltest = letterlist("CDILMVX")

rotationsymtest = letterlist("HINOSXZ")


print(rotationsymtest.lettertest("h"))
print(voweltest.lettertest("a"))
print(romannumeraltest.lettertest("c"))
print(rotationsymtest.lettertest("c"))
print(voweltest.lettertest("z"))