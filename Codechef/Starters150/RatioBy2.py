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
    x,y = mii()
    if x >= 2*y or y >= 2*x:
        print(0)
        return
    else:
        op1 = 0
        t1 =x
        t2 =y
        while t1 < 2*t2:
            op1+=1
            t1+=1
        t1=x
        t2=y
        op2=0
        while t1 < 2*t2:
            op2+=1
            t2-=1
       
        op3 = 0
        t1 = x
        t2 = y
        while t2 < 2*t1:
            t1 -= 1
            op3 +=1
            
        t1=x
        t2=y
        op4 = 0
        while t2<2*t1:
            t2 +=1
            op4 += 1
            
        print(min(op1,op2,op3,op4))
            
            


#solve()  
for _ in range(T):
    solve() 
