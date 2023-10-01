try:
    import colorama
    from colorama import Fore, Style
except ImportError:
    print("Colorama is not installed. Please install it using 'pip install colorama'")
    exit(1)
import random


class Main:
    def __init__(self) -> None:
        self.attempts = 0
        self.lower_limit = 0
        self.upper_limit = 1000
        self.rand_int = random.randint(self.lower_limit, self.upper_limit)
        colorama.init()
        self.main()

    def main(self):
        print(Fore.LIGHTBLUE_EX + f'Guess the number between {self.lower_limit} to {self.upper_limit}!' + Style.RESET_ALL)
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
                print(Fore.LIGHTRED_EX + 'Too high!' + Style.RESET_ALL)
            elif guess < self.rand_int:
                print(Fore.LIGHTYELLOW_EX + 'Too low!' + Style.RESET_ALL)
            else:
                print(Fore.LIGHTGREEN_EX + f'Correct! The number was {self.rand_int}. That took you {self.attempts} attempts' + Style.RESET_ALL)
                break


if __name__ == "__main__":
    Main()
    input()
