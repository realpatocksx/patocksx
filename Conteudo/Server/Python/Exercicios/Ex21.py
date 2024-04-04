import random

num = (random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10))

print(f'Os numero sortiados foram {num}')

maxvalor = 0
minvalor = 11

for c in num:
    if c >= maxvalor:
        maxvalor = c
    elif c <= minvalor:
        minvalor = c
print(f'O menor valor é {minvalor}')
print(f'O maior valor é {maxvalor}')

