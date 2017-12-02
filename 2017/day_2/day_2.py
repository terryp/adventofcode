
def decode(input):
    numbers = []
    with open(input, "r") as data:
        for row in data:
            elements = row.split(" ")
            elements = sorted(elements)
            elements = [e for e in elements if len(e) > 1]
            numbers.append(elements)

    return numbers

def do_math(pairs):
    nums = []

    for pair in pairs:
        for p in pair:
            p = p.replace("\n", "")
            low, high = p[0], p[-1]
            pair = sorted([low, high], reverse=True)
            nums.append(pair)
    
    sum = 0
    for num in nums:
        a, b = num
        sum += int(a) - int(b)

    return sum

if __name__ == '__main__':
    f = "./input.txt"
    raw_data = decode(f)
    print(raw_data)
    print(do_math(raw_data))
