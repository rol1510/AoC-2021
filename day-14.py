from helper import helper

testData = """
    NNCB

    CH -> B
    HH -> N
    CB -> H
    NH -> C
    HB -> C
    HC -> B
    HN -> C
    NN -> C
    BH -> H
    NC -> B
    NB -> B
    BN -> B
    BB -> N
    BC -> B
    CC -> N
    CN -> C
"""


class MappingTable:
    def __init__(self, maxDepth):
        self.data = {}
        self.maxDepth = maxDepth

    def initKey(self, key):
        self.data[key] = self.getEmptyArray()

    def addAtDepth(self, key, value, atDepth):
        assert key in self.data.keys()
        self.data[key][atDepth] = value

    def getEmptyArray(self):
        return [None for i in range(0, self.maxDepth)]


def iterateAsPairs(arr):
    for a, b in zip(arr, arr[1:len(arr)]):
        yield a, b


def getOfPair(pair, table, depth):
    pass


def step(poly, table):
    res = []
    for a, b in iterateAsPairs(poly):
        insert = table[a + b]
        res.append(a)
        res.append(insert)
        # table[a + insert + b] = a + b
    res.append(b)
    # print(len(res))
    return res


def countLetters(poly):
    counter = {}
    for p in poly:
        if p in counter.keys():
            counter[p] += 1
        else:
            counter[p] = 1
    return min(counter.values()), max(counter.values())


def brutforce(poly, table, numberOfSteps):
    for i in range(0, numberOfSteps):
        poly = step(poly, table)
        # print(f"After step {i}: {''.join(poly)}")
    return poly


def solution1(values):
    poly = values[0][0]
    table = values[1]

    mapTable = {}
    for key, value in table:
        mapTable[key] = value

    poly = brutforce(poly, mapTable, 10)
    smallest, biggest = countLetters(poly)
    print(f"res after step {10}: {biggest - smallest}")


def solution2(values):
    # What a mess!
    # thats by far the worst code if ever written
    # But I wanna code something else, so will have to do ¯\_(ツ)_/¯
    poly = values[0][0]
    table = values[1]

    print("This is gonna take a while")
    print("On my machine it's around 85 seconds")
    print("Don't look at the code. It's terrible")

    insertTable = {}
    for key, value in table:
        insertTable[key] = value

    depth10Table = {}
    for pair in insertTable.keys():
        depth10Table[pair] = brutforce([c for c in pair], insertTable, 10)

    # print(len(depth10Table['NN']))
    # resTable = {}
    # print(poly)
    # print(len(depth10Table.keys()))
    # print(depth10Table['CH'])

    print("Creating depth 20 Table")

    depth20Table = {}
    for key in insertTable.keys():
        newPoly = []
        for a, b in iterateAsPairs(depth10Table[key]):
            tmp = depth10Table[a+b]
            newPoly += tmp[:-1]
        newPoly.append(tmp[-1:][0])
        depth20Table[key] = newPoly

    print("Counting depth 20 Table")
    depth20Counter = {}
    for key in insertTable.keys():
        counter = {}
        for c in depth20Table[key]:
            if c in counter.keys():
                counter[c] += 1
            else:
                counter[c] = 1

        depth20Counter[key] = counter

    # print(depth20Counter)
    print("Counting depth 40")

    def addCounter(a, b):
        for key in b.keys():
            if key in a.keys():
                a[key] += b[key]
            else:
                a[key] = b[key]
    counter = {}
    overlap = {}

    def addOverlap(o):
        if o in overlap.keys():
            overlap[o] += 1
        else:
            overlap[o] = 1

    def removeOverlap(o):
        if o in overlap.keys():
            overlap[o] -= 1
        else:
            assert False  # should never happen

    for a, b in iterateAsPairs(poly):
        pair = a + b
        # print("top pair", pair)
        for c, d in iterateAsPairs(depth20Table[pair]):
            pairInner = c + d
            # print("inner pair", pairInner)
            coutInner = depth20Counter[pairInner]
            addCounter(counter, coutInner)
            addOverlap(d)
    removeOverlap(b)

    # print(counter)
    smallest = min(counter.values())
    biggest = max(counter.values())
    smallestKey = [key
                   for key in counter.keys() if counter[key] == smallest][0]
    biggestKey = [key
                  for key in counter.keys() if counter[key] == biggest][0]

    smallest -= overlap[smallestKey]
    biggest -= overlap[biggestKey]

    res = biggest - smallest
    print(f"res after step {40}: {res}")
    # print("overlap", overlap)
    # print("overlap sum", overlapAmount)


def get_parser():
    yield helper.split_line_parser('', helper.parse_line_as_string)
    yield helper.split_line_parser('->', helper.parse_line_as_string)


helper.runner(
    "./data/input-14.txt",
    None,
    solution1,
    solution2,
    subInputParserGenerator=get_parser,
    subInputSeperator=lambda line: line.strip() == "",
    useTestData=False,
    testData=testData
)
