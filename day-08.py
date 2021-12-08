from helper import helper
import copy

testData = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"

testData = """
    be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
    edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
    fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
    fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
    aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
    fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
    dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
    bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
    egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
    gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""

# indice mappings
#
#  0000
# 1    2
# 1    2
#  3333
# 4    5
# 4    5
#  6666
TOP = 0
TOP_LEFT = 1
TOP_RIGHT = 2
MIDDLE = 3
BOTTOM_LEFT = 4
BOTTOM_RIGHT = 5
BOTTOM = 6


def isKnownDigit(digitCode):
    if len(digitCode) == 2:
        return 1
    if len(digitCode) == 3:
        return 7
    if len(digitCode) == 4:
        return 4
    if len(digitCode) == 7:
        return 8
    return -1


class Digit:
    def __init__(self):
        self.segments = []
        for i in range(0, 7):
            self.segments.append([c for c in 'abcdefg'])

    def add(self, digitCode, digitNumber):
        if digitNumber == 1:
            self.removeDigits(digitCode, TOP)
            self.removeDigits(digitCode, TOP_LEFT)
            self.removeDigits(digitCode, MIDDLE)
            self.removeDigits(digitCode, BOTTOM_LEFT)
            self.removeDigits(digitCode, BOTTOM)

            self.onlyBeDigits(digitCode, TOP_RIGHT)
            self.onlyBeDigits(digitCode, BOTTOM_RIGHT)
        elif digitNumber == 4:
            self.removeDigits(digitCode, TOP)
            self.removeDigits(digitCode, BOTTOM_LEFT)
            self.removeDigits(digitCode, BOTTOM)

            self.onlyBeDigits(digitCode, TOP_LEFT)
            self.onlyBeDigits(digitCode, TOP_RIGHT)
            self.onlyBeDigits(digitCode, MIDDLE)
            self.onlyBeDigits(digitCode, BOTTOM_RIGHT)
        elif digitNumber == 7:
            self.removeDigits(digitCode, TOP_LEFT)
            self.removeDigits(digitCode, MIDDLE)
            self.removeDigits(digitCode, BOTTOM_LEFT)
            self.removeDigits(digitCode, BOTTOM)

            self.onlyBeDigits(digitCode, TOP)
            self.onlyBeDigits(digitCode, TOP_RIGHT)
            self.onlyBeDigits(digitCode, BOTTOM_RIGHT)
        elif digitNumber == 8:
            self.onlyBeDigits(digitCode, TOP)
            self.onlyBeDigits(digitCode, TOP_LEFT)
            self.onlyBeDigits(digitCode, TOP_RIGHT)
            self.onlyBeDigits(digitCode, MIDDLE)
            self.onlyBeDigits(digitCode, BOTTOM_LEFT)
            self.onlyBeDigits(digitCode, BOTTOM_RIGHT)
            self.onlyBeDigits(digitCode, BOTTOM)
        else:
            raise Exception("digitNumber not implemented")

    def removeDigits(self, digitsToRemove, segmentIndex):
        for digit in digitsToRemove:
            if digit in self.segments[segmentIndex]:
                self.segments[segmentIndex].remove(digit)

    def onlyBeDigits(self, digitsToKeep, segmentIndex):
        for digit in copy.copy(self.segments[segmentIndex]):
            if not digit in digitsToKeep:
                self.segments[segmentIndex].remove(digit)

    def test(self, code):
        # every not uique digit as a to and bottom
        self.onlyBeDigits(code, TOP)
        self.onlyBeDigits(code, BOTTOM)

        # every digit of len 5 also have a middle in common
        if len(code) == 5:
            self.onlyBeDigits(code, MIDDLE)

        # every digit of len 6 also ahv a top left and a bottom right in common
        if len(code) == 6:
            self.onlyBeDigits(code, TOP_LEFT)
            self.onlyBeDigits(code, BOTTOM_RIGHT)

    def getKnown(self):
        known = []
        for segment in self.segments:
            if len(segment) == 1:
                known.append(segment[0])
        return known

    def removeKnown(self):
        knwon = self.getKnown()
        for i, segment in enumerate(self.segments):
            if len(segment) >= 2:
                self.removeDigits(knwon, i)

    def removeAllKnown(self):
        # Lazy
        # Performace here!
        for i in range(0, 7):
            self.removeKnown()

    def intersect(self, other):
        new = Digit()
        for i in range(0, 7):
            new.segments[i] = [digit for digit in self.segments[i]
                               if digit in other.segments[i]]

        return new

    def isSolved(self):
        for segment in self.segments:
            if len(segment) > 1:
                return False
        return True

    # Well this function is just disgusting
    def getNumberFromCode(self, digitCode):
        assert self.isSolved()
        segmetnsActive = [0] * 7
        for i, segment in enumerate(self.segments):
            if segment[0] in digitCode:
                segmetnsActive[i] = 1

        count = sum(segmetnsActive)
        if count == 2:
            return 1
        elif count == 3:
            return 7
        elif count == 4:
            return 4
        elif count == 7:
            return 8
        else:
            ZERO = [1, 1, 1, 0, 1, 1, 1]
            TWO = [1, 0, 1, 1, 1, 0, 1]
            THREE = [1, 0, 1, 1, 0, 1, 1]
            FIVE = [1, 1, 0, 1, 0, 1, 1]
            SIX = [1, 1, 0, 1, 1, 1, 1]
            NINE = [1, 1, 1, 1, 0, 1, 1]
            if segmetnsActive == ZERO:
                return 0
            elif segmetnsActive == TWO:
                return 2
            elif segmetnsActive == THREE:
                return 3
            elif segmetnsActive == FIVE:
                return 5
            elif segmetnsActive == SIX:
                return 6
            elif segmetnsActive == NINE:
                return 9
            else:
                return -1

    def __repr__(self):
        s = ""
        for i, segment in enumerate(self.segments):
            s += str(i) + ": "
            for digit in "abcdefg":
                s += digit if digit in segment else "."
            s += "\n"
        return s


def solution1(values):
    s = 0
    for line in values:
        for digit in line[1]:
            if isKnownDigit(digit) >= 0:
                s += 1
    print(s)


def createNumber(digit, digitCodes):
    number = 0
    for i, code in enumerate(digitCodes):
        number *= 10
        number += digit.getNumberFromCode(code)
    return number


def solution2(values):
    s = 0
    for line in values:
        d = Digit()
        d2 = Digit()
        for code in (line[0] + line[1]):
            if isKnownDigit(code) >= 0:
                d.add(code, isKnownDigit(code))
            else:
                d2.test(code)

        d3 = d.intersect(d2)

        # Make sure we know the top and bottom know
        assert len(d3.segments[TOP]) == 1
        assert len(d3.segments[BOTTOM]) == 1

        d3.removeAllKnown()

        assert d3.isSolved()

        s += createNumber(d3, line[1])
    print(f"sum: {s}")


def getParser():
    p = helper.split_line_parser(' ', helper.parse_line_as_string)
    return helper.split_line_parser('|', p)


helper.runner(
    "./data/input-8.txt",
    getParser(),
    solution1,
    solution2,
    useTestData=False,
    testData=testData
)
