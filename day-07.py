from helper import helper

testData = "16,1,2,0,4,2,7,1,2,14"

# TODO: combine calcFuel* function into one


def calcFuelNeeded(values, pos):
    s = 0
    for krab in values:
        s += abs(krab - pos)
    return s


def calcFuelNeededAdvanced(values, pos):
    s = 0
    for krab in values:
        n = abs(krab - pos)
        s += n * (n+1) / 2
    return s


def solution(values, fuelFunc):
    values = sorted(values[0])
    fuelNeeded = [fuelFunc(values, pos) for pos in values]
    res = min(fuelNeeded)
    posRes = values[fuelNeeded.index(res)]
    print(f"pos={posRes} -> fuel={res}")


def solution1(values):
    solution(values, calcFuelNeeded)


def solution2(values):
    solution(values, calcFuelNeededAdvanced)


helper.runner(
    "./data/input-7.txt",
    helper.split_line_parser(',', helper.parse_line_as_int),
    solution1,
    solution2,
    useTestData=False,
    testData=testData
)
