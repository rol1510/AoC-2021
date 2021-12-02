from helper import helper

testData = """
    forward 5
    down 5
    forward 8
    up 3
    down 8
    forward 2
"""


def solution1(values):
    hPos = 0
    depth = 0

    for value in values:
        if value[0] == "forward":
            hPos += value[1]
        elif value[0] == "down":
            depth += value[1]
        elif value[0] == "up":
            depth -= value[1]

    print(f"depth: {depth} | hPos: {hPos} => {depth * hPos}")


def solution2(values):
    aim = 0
    hPos = 0
    depth = 0

    for value in values:
        if value[0] == "forward":
            hPos += value[1]
            depth += aim * value[1]
        elif value[0] == "down":
            aim += value[1]
        elif value[0] == "up":
            aim -= value[1]

    print(f"depth: {depth} | hPos: {hPos} => {depth * hPos}")


helper.runner(
    "./data/input-2.txt",
    helper.split_line_parser(' ',
                             helper.parse_line_as_string,
                             helper.parse_line_as_int),
    solution1,
    solution2,
    useTestData=False,
    testData=testData
)
