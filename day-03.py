from helper import helper
from functools import reduce

testData = """
    00100
    11110
    10110
    10111
    10101
    01111
    00111
    11100
    10000
    11001
    00010
    01010
"""


def sumBitList(a, b):
    res = []
    for x, y in zip(a, b):
        res.append(x + y)
    return res


def bitListToInt(a):
    num = 0
    for i, b in enumerate(a):
        num = (num << 1) | b
    return num


def solution1(values):
    summed = reduce(sumBitList, values)

    gammaBits = []
    for s in summed:
        diff = s - len(values)
        if(s > (len(values) / 2)):
            gammaBits.append(1)
        else:
            gammaBits.append(0)

    gamma = bitListToInt(gammaBits)
    mask = (1 << len(gammaBits)) - 1
    epsilon = (~gamma) & mask

    print(
        f"gamma: {gamma} | epsilon: {epsilon} => {gamma * epsilon}")


def filterStep(values, i, keepMostCommon):
    summed = reduce(sumBitList, values)
    oneIsMostCommon = summed[i] >= (len(values) / 2)

    if keepMostCommon == False:
        oneIsMostCommon = not oneIsMostCommon
    numberToKeep = 1 if oneIsMostCommon else 0

    filtered = filter(lambda x: True if x[i] == numberToKeep else 0, values)
    return list(filtered)


def filterValues(values, keepMostCommon):
    i = 0
    while True:
        values = filterStep(values, i, keepMostCommon)
        if(len(values) == 1):
            return values[0]
        elif (len(values) <= 0):
            raise Exception("No values left")
        i += 1


def solution2(values):
    oxygenBits = filterValues(values, True)
    co2Bits = filterValues(values, False)

    oxygen = bitListToInt(oxygenBits)
    co2 = bitListToInt(co2Bits)

    print(f"oxygen: {oxygen} | co2: {co2} => {oxygen * co2}")


# returns a list of the bits as seperat integers
def parse(line):
    line = helper.parse_line_as_string(line)
    return list(map(lambda bit: int(bit), line))


helper.runner(
    "./data/input-3.txt",
    parse,
    solution1,
    solution2,
    useTestData=False,
    testData=testData
)
