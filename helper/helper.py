
def read_lines(path):
    with open(path, "r") as file:
        return file.readlines()


def parse_lines(lines, parser):
    values = []
    for line in lines:
        values.append(parser(line))
    return values


def split_test_string(string):
    return string.strip().split('\n')


def parse_line_as_string(line):
    return line.strip()


def parse_line_as_int(line):
    return int(line.strip())


def parse_line_as_float(line):
    return float(line.strip())


# Helper function for reading & parsing of the input data file
#   testFilePath: relative path to the input data file(copied from aoc)
#   lineParseFunc: the function used to parse on line of the input file
#                  takes a line (string) as an input and returns any object
#                  e.g.: lambda line: int(line.strip())
#                        or use helper.parse_line_as_int
#   solution1: the function you implemented your solution in
#              takes an array of the parsed lines as input
#   solution2: same as solution1 ^^^
#   useTestData: bool to toggle between reading the input form the 'testFilePath'
#                or the passed 'testData' string
#   testData: A String containing some test data. Will only be used if
#             useTestData is set to True.
#             Usefull to test the solution on an smaller subset or the example


def runner(
        testFilePath,
        lineParseFunc,
        solution1,
        solution2=None,
        useTestData=False,
        testData=""):

    if useTestData:
        lines = split_test_string(testData)
    else:
        lines = read_lines(testFilePath)
    values = parse_lines(lines, lineParseFunc)

    print("------ Solution Part 1 ------")
    solution1(values)

    if solution2 != None:
        print("------ Solution Part 2 ------")
        solution2(values)
