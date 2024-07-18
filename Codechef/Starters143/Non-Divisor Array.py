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
    n = ii()
    arr = [1]
    curr_val = 1
    last_update = 1 
    for i in range(1,n):
        if i+1 == 2*last_update:
            last_update = i+1
            curr_val += 1
        arr.append(curr_val)
    print(arr[-1])
    print(*arr)
    
    
        
for _ in range(T):
    solve() 

