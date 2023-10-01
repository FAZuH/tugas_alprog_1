class Eulr:
    def __init__(self, x: float) -> None:
        self.x = x
        self.n = 0
        self.result = 0
        try:
            self.rec()
        except OverflowError:
            print('infinite')
        except RecursionError:
            print(self.result)

    def rec(self):
        self.result += (self.x ** self.n / self.factorial())
        self.n += 1
        # print(f'n={self.n}: {self.result}')
        self.rec()

    def factorial(self) -> int:
        ret = 1
        for i in range(1, self.n + 1):
            ret = ret * i
        return ret


if __name__ == "__main__":
    print('Calculator for: e to the power of x.')
    Eulr(int(input('insert x: ')))
