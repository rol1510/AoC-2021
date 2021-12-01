
def read_lines():
    with open("./input-1.txt", "r") as file:
        return file.readlines()


def parse_input(lines, parser):
    values = []
    for line in lines:
        values.append(parser(line))
    return values


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


if __name__ == "__main__":
    lines = """
      199
      200
      208
      210
      200
      207
      240
      269
      260
      263
    """.strip().splitlines()

    lines = read_lines()

    values = parse_input(lines, lambda line: int(line.strip()))
    print("--- Solution Part 1 ---")
    solution1(values)
    print("--- Solution Part 2 ---")
    solution2(values)
