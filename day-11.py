from helper import helper

testData = """
    5483143223
    2745854711
    5264556173
    6141336146
    6357385478
    4167524645
    2176841721
    6882881134
    4846848554
    5283751526
"""

# testData = """
# 11111
# 19991
# 19191
# 19991
# 11111
# """


def iterate2dPaddedRows(array, paddingSize=1):
    arr = array[paddingSize:-paddingSize] if paddingSize != 0 else array
    for y, row in enumerate(arr):
        y += paddingSize
        yield y, row


def iterate2dPaddedElements(row, paddingSize=1):
    arr = row[paddingSize:-paddingSize] if paddingSize != 0 else row
    for x, number in enumerate(arr):
        x += paddingSize
        yield x, number


def iterate2dPadded(array, paddingSize=1):
    for y, row in iterate2dPaddedRows(array, paddingSize):
        for x, number in iterate2dPaddedElements(row, paddingSize):
            yield x, y, number


OFFSET_TABLE = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def isInBounds(arr, x, y):
    xMax = len(arr)
    yMax = len(arr[0])
    return x >= 0 and x < xMax and y >= 0 and y < yMax


def saveGet(arr, x, y):
    if isInBounds(arr, x, y):
        return arr[y][x]
    else:
        return None


def saveSet(arr, x, y, value):
    if isInBounds(arr, x, y):
        arr[y][x] = value


def emptyOfSameSize(world, defaultValue):
    y = len(world)
    x = len(world[0])
    return [[defaultValue for i in range(0, x)] for j in range(0, y)]


def incrementAll(values):
    for x, y, energyLevel in iterate2dPadded(values, 0):
        values[y][x] += 1


def flash(values, x, y):
    saveSet(values, x, y, 0)
    for offset in OFFSET_TABLE:
        a = x + offset[1]
        b = y + offset[0]
        val = saveGet(values, a, b)
        if val == None:
            continue
        if val != 0:
            val += 1
        saveSet(values, a, b, val)


def step(values):
    incrementAll(values)
    didFlash = True
    flashes = 0
    while didFlash:
        didFlash = False
        for x, y, val in iterate2dPadded(values, 0):
            if val > 9:
                flash(values, x, y)
                flashes += 1
                didFlash = True
    return flashes


def solution1(values):
    flashes = 0
    steps = 100

    for i in range(0, steps):
        flashes += step(values)

    print(f"flashes: {flashes} after {steps} steps")


def solution2(values):
    gridArea = len(values) * len(values[0])
    i = 1

    while True:
        flashes = step(values)
        if flashes >= gridArea:
            print(f"All flashes synced on step {i}")
            break
        i += 1


helper.runner(
    "./data/input-11.txt",
    helper.split_line_parser('', helper.parse_line_as_int),
    solution1,
    solution2,
    useTestData=False,
    testData=testData
)
