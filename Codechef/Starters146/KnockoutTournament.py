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
    skills = lmii()
    dist = [3, 3, 4, 3, 1, 3, 3, 0, 2, 3, 2, 2, 1, 3, 2, 3]
    dist.sort()
    ans  = [[x,skills[x]] for x in range(16) ]
    
    ans.sort(key=lambda x:x[1])
    #print(ans)
    for i in range(16):
        ans[i].append(dist[i])
        
    ans.sort(key= lambda x: x[0])
    for val in ans:
        print(val[2],end=' ')
    print()
    


for _ in range(T):
    solve() 
