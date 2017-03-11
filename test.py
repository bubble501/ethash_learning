import ethash

def int_to_bytes(i):
    b = []
    for _ in range(32):
        b.append(chr(i & 0xff))
        i >>= 8
    b.reverse()
    return "".join(b)

def main():
    easy_difficulty = int_to_bytes(2**256 - 1)

main()
