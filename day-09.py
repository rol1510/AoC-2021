from helper import helper
from utility.misc import pad_2d_list

testData = """
    2199943210
    3987894921
    9856789892
    8767896789
    9899965678
"""


def iterate2dPaddedRows(array, paddingSize=1):
    for y, row in enumerate(array[paddingSize:-paddingSize]):
        y += paddingSize
        yield y, row


def iterate2dPaddedElements(row, paddingSize=1):
    for x, number in enumerate(row[paddingSize:-paddingSize]):
        x += paddingSize
        yield x, number


def iterate2dPadded(array, paddingSize=1):
    for y, row in iterate2dPaddedRows(array, paddingSize):
        for x, number in iterate2dPaddedElements(row, paddingSize):
            yield x, y, number


def computeRiskLevel(values):
    values = pad_2d_list(values, 10, 1)
    risk = 0

    for x, y, number in iterate2dPadded(values):
        outer = min(
            values[y + 1][x],
            values[y - 1][x],
            values[y][x + 1],
            values[y][x - 1],
        )
        if outer > number:
            risk += 1 + number

    return risk


def simplify(values):
    return list(map(
        lambda row: list(map(
            lambda number: 1 if number >= 9 else 0,
            row
        )),
        values
    ))


def emptyOfSameSize(world):
    y = len(world)
    x = len(world[0])
    return [[0 for i in range(0, x)] for j in range(0, y)]


def findBiggestIn2d(array):
    return max(
        [max(row) for row in array]
    )


def findConnectedStripes(basins):
    piviot = list(zip(*basins))
    connections = []

    # helper.print2dList(piviot)

    for y, row in iterate2dPaddedRows(piviot, 1):
        for x, number in iterate2dPaddedElements(row, 1):
            if number != 0:
                nextNumber = piviot[y][x+1]
                if nextNumber != 0:
                    connections.append((number, nextNumber))
                else:
                    connections.append((number, number))

    return connections


def joinConnections(connections):
    sets = []

    def findSetIndex(number):
        for i, s in enumerate(sets):
            if number in s:
                return i
        return -1

    for a, b in connections:
        indexA = findSetIndex(a)
        indexB = findSetIndex(b)

        if indexA >= 0 and indexB >= 0 and indexA != indexB:  # both known union them if needed
            setA = sets[indexA]
            setB = sets[indexB]
            newSet = set([*setA, *setB])
            sets.remove(setA)
            sets.remove(setB)
            sets.append(newSet)

        elif indexA >= 0:  # only one known
            sets[indexA].add(b)
        elif indexB >= 0:  # only one known
            sets[indexB].add(a)
        else:   # neighter known create new set
            if a != b:
                sets.append({a, b})
            else:
                sets.append({a})

    return [list(s) for s in sets]


def mergeStripes(world, joins):
    res = emptyOfSameSize(world)

    def getBasinIndex(number):
        for i, join in enumerate(joins):
            if number in join:
                # +1 needed, because not basins tiles are zeros (first one will be gone)
                return i + 1

        assert False  # Should never reach this
        return -1

    for x, y, number in iterate2dPadded(world, 1):
        if number != 0:
            index = getBasinIndex(number)
            res[y][x] = index
    return res


def mapBasins(world):
    world = pad_2d_list(world, 1)
    basins = emptyOfSameSize(world)

    lastIndex = 1

    # horizontal striping
    for y, row in iterate2dPaddedRows(world, 1):
        for x, number in iterate2dPaddedElements(row, 1):
            if number == 0:
                basins[y][x] = lastIndex
            else:
                lastIndex += 1
        lastIndex += 1

    connections = findConnectedStripes(basins)
    joins = joinConnections(connections)

    return mergeStripes(basins, joins)


def countBasinSizes(basins):
    biggest = findBiggestIn2d(basins)
    counter = [0] * biggest
    for x, y, number in iterate2dPadded(basins, 1):
        if number != 0:
            counter[number - 1] += 1
    return counter


def solution1(values):
    numberOfLowSpots = computeRiskLevel(values)
    print(numberOfLowSpots)


def solution2(values):
    world = simplify(values)
    basins = mapBasins(world)
    sizes = countBasinSizes(basins)

    threeBiggeset = sorted(sizes)[-3:]

    print(threeBiggeset[0] * threeBiggeset[1] * threeBiggeset[2])


helper.runner(
    "./data/input-9.txt",
    helper.split_line_parser('', helper.parse_line_as_int),
    solution1,
    solution2,
    useTestData=False,
    testData=testData
)
