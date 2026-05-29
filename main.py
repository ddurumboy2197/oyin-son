import random

class KompyuterOyin:
    def __init__(self):
        self.tanlangan_son = random.randint(1, 100)
        self.kushadalar = 6

    def oyna(self):
        print("Kompyuter o'ylagan sonni toping!")
        while self.kushadalar > 0:
            son = int(input("Iltimos, sonni kiriting: "))
            if son < self.tanlangan_son:
                print("Kompyuter o'ylagan son bundan katta!")
                self.kushadalar -= 1
            elif son > self.tanlangan_son:
                print("Kompyuter o'ylagan son bundan kichkina!")
                self.kushadalar -= 1
            else:
                print("Tabriklayman, siz kompyuter o'ylagan sonni topdingiz!")
                return
        print("Kompyuter o'ylagan sonni topa olmadingiz. Kompyuter o'ylagan son:", self.tanlangan_son)

oyin = KompyuterOyin()
oyin.oyna()
