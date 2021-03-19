class SumTest:

    def sumInteger(self, n):
        if n == 1:
            return n
        else:
            return n + self.sumInteger(n - 1)

    def sumInteger2(self, n):
        if n == 1:
            return n
        elif n % 2 == 0:
            return -n + self.sumInteger2(n - 1)
        else:
            return n + self.sumInteger2(n - 1)

    def frogjump(self, n):
        if n <= 2:
            return n
        else:
            return self.frogjump(n - 1) + self.frogjump(n - 2)

ob = SumTest()
print(ob.sumInteger2(10))



