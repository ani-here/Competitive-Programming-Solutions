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


dp = [0]*(2* 10**5 +1)
presum = [0]
i = 1
to_add = 0
while i <= 2*10**5:
    
    curr = i
    op = 0
    while curr != 0:
        if dp[curr] != 0:
            op += dp[curr] 
            break
        curr //= 3
        op += 1
    dp[i] = op
    to_add += op
    presum.append(to_add)
    i += 1
          
def solve():
    global dp
    global presum
    l,r = mii()
    #print(dp[:20])
    #arr = [x for x in range(l,r+1)]
    curr_l = l
    op  = 0
    op += 2*dp[l]
    #l+1 to r
    print(op + (presum[r]-presum[l]))


#solve()  
for _ in range(T):
    solve() 
