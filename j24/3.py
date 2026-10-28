class Bmi:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    @classmethod
    def calc_bmi(cls, weight, height):
        if weight > 1000:
            weight /= 1000
        if height > 100:
            height /= 100
        return cls(weight, height)

    def show_bmi(self):
        bmi = self.weight / (self.height * self.height)
        return bmi


b1 = Bmi.calc_bmi(70, 175)
print(b1.show_bmi())
