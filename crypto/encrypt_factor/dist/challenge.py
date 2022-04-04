from Crypto.Util.number import bytes_to_long, getStrongPrime

from secret import FLAG


def gen_key():
    e = 65537
    p = getStrongPrime(1024, e=e)
    q = getStrongPrime(1024, e=e)
    if q > p:
        q, p = p, q
    N = p * q
    return (N, e), (p, q)


m = bytes_to_long(FLAG)
pubkey, privkey = gen_key()
N, e = pubkey
p, q = privkey
c_flag = pow(m, e, N)
c_factor = pow(p, e, N)
print(f"{N=}")
print(f"{e=}")
print(f"{c_flag=}")
print(f"{c_factor=}")
