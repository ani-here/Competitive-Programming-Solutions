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
def solve():
    A,B,C,M = mii()
    min_dif = min(abs(A-B),abs(A-C),abs(C-B))
    if M >= min_dif:
        print("YES")
    else:
        print("NO")



for _ in range(T):
    solve() 
