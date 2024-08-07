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
    a = lmii()
    presum = []
    to_add = 0 
    ct_zeros = a.count(0)
    ct_ones = a.count(1)
    if ct_zeros == n:
        print(2*n)
        return
    
    if sum(a) == 1:
        print(ct_zeros)
        return
    
    for i in range(n):
        
        to_add += a[i]
        presum.append(to_add)
    #print(presum)
    ways = 0
    for i in range(1,n-1):
        if a[i] == 0:
            if abs(presum[i-1] - (presum[-1] - presum[i])) == 0:
                ways += 2
            if abs(presum[i-1] - (presum[-1] - presum[i])) == 1:
                ways += 1
                
    print(ways)
  


for _ in range(T):
    solve() 
