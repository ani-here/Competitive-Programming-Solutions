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
MOD = 10**9 +7
T = ii()

   


def solve():
    n,k = mii()
    a = lmii()
    for i in range(k,n-1):
        print(a[i],end=' ')
        
    print(sum(a[:k])+a[-1])
 
#solve()  
for _ in range(T):
    solve() 
