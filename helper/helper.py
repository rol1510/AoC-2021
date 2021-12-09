from copy import deepcopy
import time


def read_lines(path):
    with open(path, "r") as file:
        return file.readlines()


def parse_lines(lines, parser):
    values = []
    for line in lines:
        values.append(parser(line))
    return values


def split_sub_inputs(lines, subInputSeperator):
    subInputs = []
    current = []

    for line in lines:
        if subInputSeperator(line):
            subInputs.append(current)
            current = []
        else:
            current.append(line)
    subInputs.append(current)  # last one
    return subInputs


def split_test_string(string):
    return string.strip().split('\n')


def parse_line_as_string(line):
    return line.strip()


def parse_line_as_int(line):
    return int(line.strip())


def parse_line_as_float(line):
    return float(line.strip())


def remove_double_chars(line, char):
    d = char * 2
    while line.find(d) >= 0:
        line = line.replace(d, char)
    return line


# will return a parse function to parse a list of inputs
# See day-02.py for usage
def split_line_parser(seperator, *args):
    def parser(line):
        if seperator != "":
            parts = line.strip().split(seperator)
        else:
            parts = [c for c in line.strip()]
        values = []
        for i, part in enumerate(parts):
            values.append(args[i % len(args)](part))
        return values
    return parser


#   testFilePath:   relative path to the input data file(copied from aoc)
#   lineParseFunc:  the function used to parse on line of the input file
#                   takes a line (string) as an input and returns any object
#                   e.g.: lambda line: int(line.strip())
#                        or use helper.parse_line_as_int
#   solution1:      the function you implemented your solution in
#                   takes an array of the parsed lines as input
#   solution2:      same as solution1 ^^^
#   subInputSeperator:       function that takes a line as argument and
#                            returns True if this line should splits the sub-input
#                            if used 'subInputParserGenerator' needs to be set
#                            see day-04.py for more info
#   subInputParserGenerator: needed only if 'subInputSeperator' is set
#                            expects a generator function which returns the
#                            parsers for the next sub input
#   useTestData:    bool to toggle between reading the input form the 'testFilePath'
#                   or the passed 'testData' string
#   testData:       A String containing some test data. Will only be used if
#                   useTestData is set to True.
#                   Usefull to test the solution on an smaller subset or the example
def runner(
        testFilePath,
        lineParseFunc,
        solution1,
        solution2=None,
        subInputSeperator=None,
        subInputParserGenerator=None,
        useTestData=False,
        testData=""):

    if useTestData:
        lines = split_test_string(testData)
    else:
        lines = read_lines(testFilePath)

    values = []
    if subInputSeperator != None:
        subInputs = split_sub_inputs(lines, subInputSeperator)
        gen = subInputParserGenerator()
        for i, si in enumerate(subInputs):
            values.append(parse_lines(si, next(gen)))
    else:
        values = parse_lines(lines, lineParseFunc)

    startTime = time.time()
    print("------ Solution Part 1 ------")
    solution1(deepcopy(values))
    timePassed = time.time() - startTime
    print(f"------- Took {round(timePassed * 1000, 2)}ms -------")
    print()

    if solution2 != None:
        startTime = time.time()
        print("------ Solution Part 2 ------")
        solution2(deepcopy(values))
        timePassed = time.time() - startTime
        print(f"------- Took {round(timePassed * 1000, 2)}ms -------")
