import random
import string


def random_string(min_len=1, max_len=255, cyr=False):
    length = random.randint(min_len, max_len)
    symbols = string.printable[:-2] + " "*10
    if cyr:
        symbols += ''.join([chr(l) for l in range(0x0410, 0x0458) if chr(l).isprintable()])
    return ''.join(random.choices(string.printable[:-2], k=length))



if __name__ == "__main__":
    print(random_string())
    # print(string.printable)
    # print(string.whitespace)
    # print(string.ascii_letters, string.digits, string.punctuation)
    # print(random.random())
    # print(random.randint(10, 99))
    # print(random.randrange(1, 100, 2))
    # print(random.choice("sdzfgchbkjbk"))
    # print(random.choices(["a", "bb", "x"], k=10))