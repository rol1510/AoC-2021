from helper import helper
from functools import reduce

testData = """
    7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

    22 13 17 11  0
    8  2 23  4 24
    21  9 14 16  7
    6 10  3 18  5
    1 12 20 15 19

    3 15  0  2 22
    9 18 13 17  5
    19  8  7 25 23
    20 11 10 24  4
    14 21 16 12  6

    14 21 17 24  4
    10 16 15  9 19
    18  8 23 26 20
    22 11 13  6  5
    2  0 12  3  7
"""


def find(arr, e):
    for i, a in enumerate(arr):
        if a == e:
            return i
    return -1


def replace(row, number, replacement=None):
    while True:
        x = find(row, number)
        if x >= 0:
            row[x] = replacement
        else:
            break


def replace_number(boards, number, replacement=None):
    for board in boards:
        for row in board:
            replace(row, number, replacement)


def test_row(row):
    for e in row:
        if not e is None:
            return False
    return True


def test_rows(board):
    for row in board:
        if test_row(row) == True:
            return True
    return False


def test_columns(board):
    piviot = list(zip(*board))
    return test_rows(piviot)


def bingo(boards):
    for i, board in enumerate(boards):
        if test_rows(board) or test_columns(board):
            return i
    return -1


def last_bingo(boards):
    bingos = []
    for i, board in enumerate(boards):
        bingos.append(test_rows(board) or test_columns(board))

    if sum(bingos) >= (len(bingos) - 1):
        return find(bingos, False)
    else:
        return -1


def calc_score(board, lastDraw):
    sum = 0
    for row in board:
        for e in row:
            if not e is None:
                sum += e
    return sum * lastDraw


def solution1(values):
    draws = values[0][0]
    boards = values[1:]

    for draw in draws:
        replace_number(boards, draw)

        i = bingo(boards)
        if i >= 0:
            print("Bingo! ", calc_score(boards[i], draw))
            break


def solution2(values):
    draws = values[0][0]
    boards = values[1:]

    for i, draw in enumerate(draws):
        replace_number(boards, draw)

        bingo = last_bingo(boards)
        if bingo >= 0:
            # interate once more to calculate the score of the right state
            replace_number(boards, draws[i+1])
            print("Last Bingo! ", calc_score(boards[bingo], draws[i+1]))
            break


def get_parser():
    parse_numbers = helper.split_line_parser(',', helper.parse_line_as_int)

    def get_parse_bingo_board():
        splitLine = helper.split_line_parser(' ', helper.parse_line_as_int)
        return lambda line: splitLine(helper.remove_double_chars(line, ' '))

    yield parse_numbers
    while True:
        yield get_parse_bingo_board()


helper.runner(
    "./data/input-4.txt",
    None,
    solution1,
    solution2,
    subInputParserGenerator=get_parser,
    subInputSeperator=lambda line: line.strip() == "",
    useTestData=False,
    testData=testData
)
