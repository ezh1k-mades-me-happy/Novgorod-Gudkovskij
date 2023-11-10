import sys

s = 0
for line in sys.stdin:
    for i in line.rstrip('\n').lower().split():
        if 'далек' == i[:5]:
            s += 1
            break
print(s)
