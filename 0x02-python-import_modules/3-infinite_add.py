#!/usr/bin/python3
import sys

if __name__ == "__main__":
    ans = 0
    for av in sys.argv:
        if av != sys.argv[0]:
            ans += int(av)
    print(ans)
