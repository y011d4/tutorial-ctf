import random

from secret import FLAG


class LFSR:
    def __init__(self):
        self.state = random.choices([0, 1], k=32)
        assert len(self.state) == 32

    def _step(self):
        s = self.state[0] ^ self.state[2] ^ self.state[6] ^ self.state[7]
        self.state[:31] = self.state[1:32]
        self.state[31] = s
        return s

    def rand_char(self):
        res = 0
        for _ in range(8):
            res *= 2
            _ = self._step()  # skip one step to make it secure!
            res += self._step()
        return res


if __name__ == "__main__":
    assert FLAG.startswith(b"FLAG{")
    lfsr = LFSR()
    enc = b""
    for i in range(len(FLAG)):
        enc += bytes([FLAG[i] ^ lfsr.rand_char()])
    print(f"{enc = }")
