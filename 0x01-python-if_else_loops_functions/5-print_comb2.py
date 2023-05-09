#!/usr/bin/python3
print(*["{:0>2d}".format(i) if i != 99 else str(i) for i in range(100)], sep=", ")
