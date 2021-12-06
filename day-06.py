from helper import helper

testData = "3,4,3,1,2"


def bucketInitialValues(values):
    count = [0] * (max(values) + 1)
    for fish in values:
        count[fish] += 1

    # [[daysLeft, numberOfFish], ...]
    res = []
    for i, c in enumerate(count):
        if c >= 1:
            res.append([i, c])
    return res


def step(buckets):
    newFish = []
    for bucket in buckets:
        bucket[0] -= 1
        if bucket[0] < 0:
            bucket[0] = 6
            newFish.append([8, bucket[1]])

    for fish in newFish:
        buckets.append(fish)


def mergeBuckets(buckets):
    pivot = list(zip(*buckets))
    count = [0] * (max(pivot[0]) + 1)
    for bucket in buckets:
        count[bucket[0]] += bucket[1]

    # [[daysLeft, numberOfFish], ...]
    res = []
    for i, c in enumerate(count):
        if c >= 1:
            res.append([i, c])
    return res


def sumFish(buckets):
    pivot = list(zip(*buckets))
    return sum(pivot[1])


def simulate(values, days):
    buckets = bucketInitialValues(values[0])

    for i in range(0, days):
        step(buckets)

        if i % 10 == 0:
            buckets = mergeBuckets(buckets)

    print(f"After {days} days we'll have {sumFish(buckets)} fish!!!")


def solution1(values):
    simulate(values, 80)


def solution2(values):
    simulate(values, 256)
    simulate(values, 1024)
    simulate(values, 1024*16)


helper.runner(
    "./data/input-6.txt",
    helper.split_line_parser(',', helper.parse_line_as_int),
    solution1,
    solution2,
    useTestData=False,
    testData=testData
)
