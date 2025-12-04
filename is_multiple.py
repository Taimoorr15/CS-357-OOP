class Is_Multiple:
    def __init__(self, n, m):
        try:
            self._n = int(n)
            self._m = int(m)
        except ValueError:
            raise ValueError("Both n and m must be integers!")

    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, other):
        if isinstance(other, int):  # check integer
            self._n = other
        else:
            raise ValueError(f"{other} must be an integer")

    @property
    def m(self):
        return self._m

    @m.setter
    def m(self, other):
        if isinstance(other, int):  # check integer
            self._m = other
        else:
            raise ValueError(f"{other} must be an integer")

    def check_multiple(self):
        if self._n % self._m == 0:
            return f"{self._n} is a multiple of {self._m} ({self._m} * {self._n // self._m})"
        else:
            return f"{self._n} is not a multiple of {self._m}"
