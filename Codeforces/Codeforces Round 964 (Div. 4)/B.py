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
    a1,a2,b1,b2 = mii()

    wins = 0
    if a1 >= b1 and a2 >  b2 or a1 > b1 and a2 >=  b2 :
        wins += 2
    
    if a1 >= b2 and a2 > b1 or a1 > b2 and a2 >= b1 :
        wins += 2


    print(wins)



#solve()  
for _ in range(T):
    solve() 
