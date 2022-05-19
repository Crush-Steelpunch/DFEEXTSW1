class Letterlist:

    def __init__(self,letterset="AEIOU"):
        self.listofletter = letterset

    def lettertest(self, invar):
        if invar.upper() in self.listofletter:
            return True
        else:
            return False




voweltest = Letterlist()

romannumeraltest = Letterlist("CDILMVX")

rotationsymtest = Letterlist("HINOSXZ")

print(voweltest.listofletter)                #this is the same
print(getattr(voweltest, "listofletter"))      # as doing this
print(rotationsymtest.lettertest("h"))
print(voweltest.lettertest("a"))
print(romannumeraltest.lettertest("c"))
print(rotationsymtest.lettertest("c"))
print(voweltest.lettertest("z"))