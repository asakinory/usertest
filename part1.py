import random
def part1(args, hkubeapi):
    print('algorithm: range start')
    input = args['input'][0]
    array = [random.random() for _ in range(input)]
    return array