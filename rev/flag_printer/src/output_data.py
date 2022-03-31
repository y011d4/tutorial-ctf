from Crypto.Util.number import bytes_to_long

flag = b"FLAG{python_ha_waruku_nai}"

data = []
for i in range(1, len(flag) + 1):
    tmp = bytes_to_long(flag[:i])
    data.append((tmp - 1) * tmp // 2)
print(data)
