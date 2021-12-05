from helper import helper

testData = """
    0,9 -> 5,9
    8,0 -> 0,8
    9,4 -> 3,4
    2,2 -> 2,1
    7,0 -> 7,4
    6,4 -> 2,0
    0,9 -> 2,9
    3,4 -> 1,4
    0,0 -> 8,8
    5,5 -> 8,2
"""


def isStraight(line):
    x1, y1, x2, y2 = line
    return x1 == x2 or y1 == y2


def findMinBoardSize(lines):
    x1s, y1s, x2s, y2s = list(zip(*lines))
    return (
        min(x1s + x2s),
        min(y1s + y2s),
        max(x1s + x2s),
        max(y1s + y2s),
    )


def initBoard(size):
    minX, minY, maxX, maxY = size
    assert minX >= 0
    assert minY >= 0

    maxX += 1
    maxY += 1

    board = []
    for y in range(0, maxY):
        row = []
        for x in range(0, maxX):
            row.append(0)
        board.append(row)
    return board


def smallerFirst(a, b):
    if a <= b:
        return (a, b)
    else:
        return (b, a)


def drawLineX(board, x1, x2, y):
    x1, x2 = smallerFirst(x1, x2)
    for x in range(x1, x2 + 1):
        board[y][x] += 1


def drawLineY(board, y1, y2, x):
    y1, y2 = smallerFirst(y1, y2)
    for y in range(y1, y2 + 1):
        board[y][x] += 1


def drawLineDiagonal(board, line):
    x1, y1, x2, y2 = line

    xdir = 1 if x1 <= x2 else -1
    ydir = 1 if y1 <= y2 else -1

    x = x1
    y = y1
    board[y][x] += 1

    while x != x2 or y != y2:
        x += xdir
        y += ydir
        board[y][x] += 1


def drawStraightLine(board, line):
    x1, y1, x2, y2 = line

    if y1 == y2:
        drawLineX(board, x1, x2, y1)
    elif x1 == x2:
        drawLineY(board, y1, y2, x1)


def printBoard(board):
    for row in board:
        print(row)


def count(board, minValue):
    s = 0
    for row in board:
        for number in row:
            if number >= minValue:
                s += 1
    return s


def solution1(values):
    validLines = [line for line in values if isStraight(line)]
    boardSize = findMinBoardSize(validLines)
    board = initBoard(boardSize)

    for line in validLines:
        drawStraightLine(board, line)

    # printBoard(board)
    print(f"2 or higher {count(board, 2)} times")


def solution2(values):
    boardSize = findMinBoardSize(values)
    board = initBoard(boardSize)

    for line in values:
        if isStraight(line):
            drawStraightLine(board, line)
        else:
            drawLineDiagonal(board, line)

    # printBoard(board)
    print(f"2 or higher {count(board, 2)} times")


def parser(line):
    line = line.replace('->', ',').split(',')
    return [int(x.strip()) for x in line]


helper.runner(
    "./data/input-5.txt",
    parser,
    solution1,
    solution2,
    useTestData=False,
    testData=testData
)
