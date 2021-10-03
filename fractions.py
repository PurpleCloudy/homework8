class Fraction:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    def get_numerator(self):
        return self.numer
    def get_denominator(self):
        return self.denom
    def __str__(self):
        return f'{self.numer} / {self.denom}'
    def __add__(self, adder):
        new_n = self.numer * adder.denom + self.denom * adder.numer
        new_d = self.denom * adder.denom
        return Fraction(new_n, new_d)
    def __sub__(self, subber):
        new_n = self.numer * subber.denom - self.denom * subber.numer
        new_d = self.denom * subber.denom
        return Fraction(new_n, new_d)
    def __mul__(self, muller):
        new_n = (self.numer * muller.denom) * (self.denom * muller.numer)
        new_d = self.denom * muller.denom
        return Fraction(new_n, new_d)
    def __div__(self, divver):
        new_n = (self.numer * divver.denom) * (self.denom * divver.numer)
        new_d = self.denom * divver.numer
        return Fraction(new_n, new_d)
oneHalf = Fraction(1,2)
threee = Fraction(1,3)
print(oneHalf + threee)
print(oneHalf - threee)
print(oneHalf * threee)
print(oneHalf.__div__(threee))