class Quantity:
    def __init__(self, amount, unit):
        self.amount = amount
        self.unit = unit

    def times(self, multiplier):
        return Quantity(self.amount * multiplier, self.unit)

    def plus(self, other):
        return Sum(self, other)

    def __eq__(self, other):
        return self.amount == other.amount and self.unit == other.unit

    def __repr__(self):
        return f"Quantity({self.amount}, {self.unit!r})"


class Sum:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def times(self, multiplier):
        return Sum(
            self.left.times(multiplier),
            self.right.times(multiplier)
        )

    def reduce(self, unit):
        left_amount = self.left.amount
        right_amount = self.right.amount

        if self.left.unit == "g" and self.right.unit == "oz":
            right_amount = self.right.amount * 28.3495

        if self.left.unit == "oz" and self.right.unit == "g":
            left_amount = self.left.amount * 28.3495

        return Quantity(left_amount + right_amount, unit)


class Converter:
    def reduce(self, expression, unit):
        return expression.reduce(unit)
