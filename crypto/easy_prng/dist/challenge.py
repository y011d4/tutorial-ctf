import random

from Crypto.Util.number import isPrime

from secret import FLAG


class PRNG:
    def __init__(self):
        self.state = random.randint(0, 2 ** 128)
        self.p = random.randint(0, 2 ** 128)
        while not isPrime(self.p):
            self.p = random.randint(0, 2 ** 128)
        self.a = random.randint(0, 2 ** 128)
        self.b = random.randint(0, 2 ** 128)

    def __call__(self):
        self.state = (self.state * self.a + self.b) % self.p
        return self.state


prng = PRNG()

while True:
    print("guess?> ", end="", flush=True)
    inp = input()
    if inp == "exit":
        break
    guess: int
    try:
        guess = int(inp)
    except ValueError:
        print("You should input number")
        continue
    r = prng()
    if guess == r:
        print(f"Success! The flag is {FLAG}")
    else:
        print(f"{r}")
