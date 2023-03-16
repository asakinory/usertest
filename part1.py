import random

def start(args):
    return part1(args['input'][0])

def part1(num):
    print('algorithm range started')
    array = [random.random() for _ in range(num)]
    return array