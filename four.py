import itertools

for i in itertools.product('0123456789', repeat=4):
    print(''.join(i))
