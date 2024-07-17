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
    n,x = mii()
    coins = 0
    for i in range(x):
        coins += 2**(n-i)
    for i in range(1,n-x+1):
        coins -= 2**(i)
        
    print(coins)
        
        
for _ in range(T):
    solve() 

