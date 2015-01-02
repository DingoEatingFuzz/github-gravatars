from random import shuffle

seeds = [str(x) for x in range(2**15)]
shuffle(seeds)

with open('seeds.txt', 'w') as f:
    f.write(str('\n').join(seeds))
