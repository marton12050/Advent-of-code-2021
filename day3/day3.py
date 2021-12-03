def task1(bitsdata):
    counts = [0] * len(bitsdata[0])
    for binumber in bitsdata:
        for bit in range(len(bitsdata[0])):
            if binumber[bit] == "1":
                counts[bit] += 1

    gamma = ""
    for bit in counts:
        gamma += "1" if bit > len(data)/2 else "0"
    gamma = int(gamma, 2)
    epsilon = 2**(len(data[0])) - gamma - 1

    return gamma * epsilon

def splitting(binaries, pos):
    ones = []
    zeros = []
    for x in binaries:
        (ones if x[pos] == '1' else zeros).append(x)

    return ones, zeros


def task2(binaries, pred):
    for pos in range(len(binaries[0])):
        if len(binaries) == 1:
            return binaries[0]
        ones, zeros = splitting(binaries, pos)
        binaries = (ones if pred(len(ones), len(zeros)) else zeros)


data = open("input.txt", "r").read().splitlines()
print(task1(data))
print(int(task2(data, (lambda x, y : x >= y)),2) * int(task2(data, (lambda x, y : x < y)),2))