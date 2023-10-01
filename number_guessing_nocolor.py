import random


class Main:
    def __init__(self) -> None:
        self.attempts = 0
        self.lower_limit = 0
        self.upper_limit = 1000
        self.rand_int = random.randint(self.lower_limit, self.upper_limit)
        self.main()

    def main(self):
        print(f'Guess the number between {self.lower_limit} to {self.upper_limit}!')
        while True:
            self.attempts += 1
            try:
                guess = int(input('> '))
            except Exception as e:
                print(e)
                continue

            if guess == 'stop':
                break
            if guess > self.rand_int:
                print('Too high!')
            elif guess < self.rand_int:
                print('Too low!')
            else:
                print(f'Correct! The number was {self.rand_int}. That took you {self.attempts} attempts')
                break


if __name__ == "__main__":
    Main()
