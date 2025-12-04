class cuddly_toy:
    def __init__(self, job, colour, size):
        self.job = job
        self.colour = colour
        self.size = size

    def noise(self):
        return "This toy makes a generic cuddly toy sound."

    def describe_itself(self):
        return f"I have a job of {self.job}, my colour is {self.colour}, and my size is {self.size}."


class teddy(cuddly_toy):
    def __init__(self, job, colour, size):
        super().__init__(job, colour, size)

    def noise(self):
        return "Teddy says: Growl!"


class bunny(cuddly_toy):
    def __init__(self, job, colour, size):
        super().__init__(job, colour, size)

    def noise(self):
        return "Bunny says: Squeak!"


class engine_drivers(teddy):
    def __init__(self, size):
        super().__init__("Engine Driver", "Blue", size)


class gardeners(teddy):
    def __init__(self, size):
        super().__init__("Gardener", "Red", size)


class clown(bunny):
    def __init__(self, size):
        super().__init__("Clown", "White", size)


class bank_manager(bunny):
    def __init__(self, size):
        super().__init__("Bank Manager", "Black", size)


toy1 = engine_drivers("Medium")
print(toy1.describe_itself())
print(toy1.noise())

toy2 = clown("Large")
print(toy2.describe_itself())
print(toy2.noise())
