import random
# a + 2b + 3c + 4d = 30


def foo(a, b, c, d):
    return a + 2*b + 3*c + 4*d - 30


def fitness(a, b, c, d):
    ans = foo(a, b, c, d)

    if (ans == 0):
        return 999999
    else:
        return abs(1/ans)


solutions = []
for s in range(1000):
    # defining the initial populatuion
    solutions.append(
        (
            random.uniform(0, 10000),
            random.uniform(0, 10000),
            random.uniform(0, 10000),
            random.uniform(0, 10000)
        )
    )
for i in range(100000):
    rankedsolutions = []
    for s in solutions:
        # rankedsolutions with fitness value and tuple associated with it
        rankedsolutions.append((fitness(s[0], s[1], s[2], s[3]), s))
    rankedsolutions.sort()
    rankedsolutions.reverse()
    print(f"=====gen {i} best solutions ======")
    # if reached optimum solution break
    print(rankedsolutions[0])
    if rankedsolutions[0][0] > 9999:
        break
    # selection
    bestsolutions = rankedsolutions[:100]

    elements = []
    for s in bestsolutions:
        elements.append(s[1][0])
        elements.append(s[1][1])
        elements.append(s[1][2])
        elements.append(s[1][3])
        # elements.append(s[1][1])

    newGen = []
    # mutate
    for _ in range(1000):
        e1 = random.choice(elements) * random.uniform(0.99, 1.01)
        e2 = random.choice(elements) * random.uniform(0.99, 1.01)
        e3 = random.choice(elements) * random.uniform(0.99, 1.01)
        e4 = random.choice(elements) * random.uniform(0.99, 1.01)
        newGen.append((e1, e2, e3, e4))
    solutions = newGen
# print(solutions[:5])
