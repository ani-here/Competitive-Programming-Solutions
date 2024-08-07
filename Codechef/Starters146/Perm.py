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
    arr = [0]*n
    to_put = 1
    j = n-1
    while j >= 0:
        arr[j] = to_put
        j -= 2
        to_put += 1
        
    for i in range(n):
        if arr[i] == 0:
            arr[i] = to_put
            to_put += 1
            
    print(*arr)




for _ in range(T):
    solve() 
