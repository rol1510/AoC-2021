from helper import helper

testData = """
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""


BRACKET_MAPPER = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",

    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}

BRACKET_SCORES_PART_1 = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

BRACKET_SCORES_PART_2 = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def isOpeningBracket(char):
    return char in ["(", "[", "{", "<"]


def findIllegal(line):
    stack = []
    for c in line:
        if isOpeningBracket(c):
            stack.append(BRACKET_MAPPER[c])
        else:
            if stack[-1] == c:
                stack.pop()
            else:
                return c
    return None


def isIncompleteLine(line):
    return findIllegal(line) == None


def findClosingBrackets(line):
    stack = []

    for c in line:
        if isOpeningBracket(c):
            stack.append(BRACKET_MAPPER[c])
        else:
            assert stack[-1] == c  # invalid closing bracket in string
            stack.pop()

    return ''.join(stack[::-1])


def calcScorePart2(brackets):
    score = 0
    for c in brackets:
        score *= 5
        score += BRACKET_SCORES_PART_2[c]
    return score


def solution1(values):
    res = 0

    for line in values:
        illegalChar = findIllegal(line)
        if illegalChar != None:
            res += BRACKET_SCORES_PART_1[illegalChar]

    print(res)


def solution2(values):
    scores = []
    for line in values:
        if isIncompleteLine(line):
            res = findClosingBrackets(line)
            scores.append(calcScorePart2(res))

    scores = sorted(scores)
    print(scores[len(scores) // 2])


helper.runner(
    "./data/input-10.txt",
    helper.parse_line_as_string,
    solution1,
    solution2,
    useTestData=False,
    testData=testData
)
