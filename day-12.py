from helper import helper
from copy import copy

# part1: 10 paths
# part2: 36 paths
testData = """
    start-A
    start-b
    A-c
    A-b
    b-d
    A-end
    b-end
"""

# part1: 19 paths
# part2: 103 paths
testData = """
    dc-end
    HN-start
    start-kj
    dc-start
    dc-HN
    LN-dc
    HN-end
    kj-sa
    kj-HN
    kj-dc
"""

# # part1: 226 paths
# testData = """
#     fs-end
#     he-DX
#     fs-he
#     start-DX
#     pj-DX
#     end-zg
#     zg-sl
#     zg-pj
#     pj-he
#     RW-he
#     fs-DX
#     pj-RW
#     zg-RW
#     start-pj
#     he-WI
#     zg-he
#     pj-fs
#     start-RW
# """

NAME_TO_ID_TABEL = {}


def get_id(name):
    global NAME_TO_ID_TABEL
    if not name in NAME_TO_ID_TABEL.keys():
        NAME_TO_ID_TABEL[name] = max([-1, *NAME_TO_ID_TABEL.values()]) + 1

    return NAME_TO_ID_TABEL[name]


class Cave:
    def __init__(self, name):
        self.name = name
        self.id = get_id(name)
        self.isBig = name.isupper()
        self.neighbours = []
        self.isStart = name == "start"
        self.isEnd = name == "end"

    def addNeighbour(self, otherCave):
        self.neighbours.append(otherCave)
        otherCave.neighbours.append(self)

    def __repr__(self):
        return f"(id: {self.id}, name: {self.name}, ns: {[c.name for c in self.neighbours]})"


def parse_caves(values):
    caves = []

    def add(name):
        if not name in [c.name for c in caves]:
            caves.append(Cave(name))

    def get_cave(name):
        for c in caves:
            if c.name == name:
                return c
        return None

    def connect(nameA, nameB):
        cA = get_cave(nameA)
        cB = get_cave(nameB)
        assert cA != None and cB != None  # both caves should already be in the list
        cA.addNeighbour(cB)

    for val in values:
        add(val[0])
        add(val[1])

    for val in values:
        connect(val[0], val[1])

    return caves


def explore_paths_part_1(cave, path):
    path = copy(path)
    path.append(cave.id)
    if cave.isEnd:
        return 1

    pathsFound = 0

    for next in cave.neighbours:
        # if the next cave is small and was already visited, don't visit it
        if next.isBig == False and next.id in path:
            continue
        pathsFound += explore_paths_part_1(next, path)

    return pathsFound


# returns (targetVisits, mostVisits)
def smallCaveNumberOfVisits(path, targetId):
    counter = {}
    for cave in path:
        if cave.isBig == False and cave.isStart == False and cave.isEnd == False:
            if not cave.id in counter.keys():
                counter[cave.id] = 1
            else:
                counter[cave.id] += 1

    mostVisits = max([0, *counter.values()])
    if targetId in counter.keys():
        targetVisits = counter[targetId]
    else:
        targetVisits = 0

    return targetVisits, mostVisits


def explore_paths_part_2(cave, path):
    path = copy(path)
    path.append(cave)

    if cave.isEnd:
        return 1

    pathsFound = 0

    for next in cave.neighbours:
        if next.isStart:
            continue
        # if the next cave is small and was already visited, don't visit it
        if next.isBig == False:
            targetVisits, mostVisits = smallCaveNumberOfVisits(path, next.id)
            if mostVisits >= 2 and targetVisits >= 1:
                continue

        pathsFound += explore_paths_part_2(next, path)

    return pathsFound


def solution1(values):
    caves = parse_caves(values)
    startCave = [c for c in caves if c.isStart][0]
    res = explore_paths_part_1(startCave, [])
    print(res)


def solution2(values):
    caves = parse_caves(values)
    startCave = [c for c in caves if c.isStart][0]
    res = explore_paths_part_2(startCave, [])
    print(res)


helper.runner(
    "./data/input-12.txt",
    helper.split_line_parser('-', helper.parse_line_as_string),
    solution1,
    solution2,
    useTestData=False,
    testData=testData
)
