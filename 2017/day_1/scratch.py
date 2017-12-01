
def captcha(digits, offset=1):
    neighbors = digits[offset:] + digits[:offset]
    print(digits)
    print(neighbors)
    for d, n in zip(digits, neighbors):
        print(d, n)
    # return sum(int(d) for d, n in zip(digits, neighbors) if d == n)

if __name__ == '__main__':
    captcha("91212129")
