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
    n = ii()
    freq = defaultdict(int)
    freq[0] = n
    curr_ans = 0 
    max_freq = 0
    max_no = -1
    for _ in range(n):
        x,y = mii()
        freq[y] += 1
        if freq[y] > max_freq:
            max_no = y
            max_freq = freq[y]
        freq[0] -= 1
        curr_ans += freq[y]*(freq[y]-1)//2
        curr_ans -= max(0,(freq[y]-1)*(freq[y]-2)//2)
        
        tc = freq[0] + max_freq
        print((curr_ans - max_freq*(max_freq-1)//2) + tc*(tc-1)//2,end = ' ')
        
    print()

for _ in range(T):
  solve()
