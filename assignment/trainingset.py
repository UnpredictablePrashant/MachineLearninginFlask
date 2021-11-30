from random import randint
TRAIN_SET_LIMIT = 1000
TRAIN_SET_COUNT = 100

TRAIN_INPUT = list()
TRAIN_OUTPUT = list()
for i in range(TRAIN_SET_COUNT):
    a = randint(0, TRAIN_SET_LIMIT)
    b = randint(0, TRAIN_SET_LIMIT)
    c = randint(0, TRAIN_SET_LIMIT)
    d = randint(0, TRAIN_SET_LIMIT)
    e = randint(0, TRAIN_SET_LIMIT)
    op = a + (1*b) - (10*c) + (50*d) - e 
    TRAIN_INPUT.append([a, b, c, d, e])
    TRAIN_OUTPUT.append(op)