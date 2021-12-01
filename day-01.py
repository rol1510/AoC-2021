from helper import helper


def solution1(values):
    last = values[0]
    count = 0
    for next in values[1:]:
        if next - last > 0:
            count += 1
        last = next
    print(count)


def solution2(values):
    def sumRange(index):
        return sum(values[index: index+3])

    last = sumRange(0)
    count = 0

    for i, _ in enumerate(values[1:-1]):
        next = sumRange(i)
        if next - last > 0:
            count += 1
        last = next

    print(count)


helper.runner(
    "./data/input-1.txt",
    helper.parse_line_as_int,
    solution1,
    solution2
)
