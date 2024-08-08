from collections import defaultdict
from collections import deque
from itertools import permutations
from math import *

 
import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lmii = lambda: list(map(int, input().split()))
tmii = lambda: tuple(map(int, input().split()))
mfi = lambda: map(float, input().split())
lmfi = lambda: list(map(float, input().split()))

T = ii()
ct = 0


def solve():
    n,s,m = mii()
    mat = []
    for _ in range(n):
        mat.append(lmii())

    start = 0
    for intr in mat:
        if  intr[0]-start >= s:
            print("YES")
            return
        start = intr[1]
    if m - start >= s:
        print("YES")
        return 
    print("NO")


#solve()  
for _ in range(T):
    solve() 
