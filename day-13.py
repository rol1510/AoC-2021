from helper import helper
from copy import copy
import re

testData = """
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""


def fold(points, foldInfo):
    axisIndex = 0 if foldInfo[0] == 'x' else 1
    pos = foldInfo[1]

    for p in points:
        if p[axisIndex] > pos:
            p[axisIndex] = pos - (p[axisIndex] - pos)


def mergePoints(points):
    points = sorted(points)

    def equal(p1, p2):
        return p1[0] == p2[0] and p1[1] == p2[1]

    i = 0
    while i < (len(points) - 1):
        p1 = points[i]
        p2 = points[i+1]
        if equal(p1, p2):
            points.remove(p2)
        else:
            i += 1

    return points


def renderPoints(points):
    maxX = max([p[0] for p in points]) + 1
    maxY = max([p[1] for p in points]) + 1
    render = [[' ' for i in range(0, maxX)] for j in range(0, maxY)]

    for x, y in points:
        render[y][x] = '#'

    printRender(render)


def printRender(render):
    s = ""
    for row in render:
        for char in row:
            s += char
        s += "\n"
    print(s)


def solution1(values):
    points, folds = values
    fold(points, folds[0])
    points = mergePoints(points)
    print("points visible after first fold:", len(points))


def solution2(values):
    points, folds = values
    for foldInfo in folds:
        fold(points, foldInfo)
    points = mergePoints(points)
    renderPoints(points)


def get_parser():
    parse_coord = helper.split_line_parser(',', helper.parse_line_as_int)

    def parse_fold(line):
        print(line)
        res = re.findall("([xy])=(\d+)", line)
        assert len(res) == 1
        xy, pos = res[0]
        return xy, int(pos)

    yield parse_coord
    yield parse_fold


helper.runner(
    "./data/input-13.txt",
    None,
    solution1,
    solution2,
    subInputParserGenerator=get_parser,
    subInputSeperator=lambda line: line.strip() == "",
    useTestData=False,
    testData=testData
)
