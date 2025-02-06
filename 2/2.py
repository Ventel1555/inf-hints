from itertools import product, permutations

def F(x, y, z, w):
    return x and y and z or w

for i in product([0, 1], repeat=2):
    t = ((i[0], 1, i[1], 1),
         (1, 1, 1, 1),
         (1, 1, 0, 1))
    if len(t)==len(set(t)):
        for p in permutations('xyzw'):
            if [F(**dict(zip(p, r))) for r in t] == [1,1,1]:
                print(*p)