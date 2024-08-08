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
    s = list(input())
    #print(s)
    t =list(input())
    
    dum = "a"
    ptr_t = 0
    for i in range(len(s)):
        if s[i] == t[ptr_t]:
            s[i] = t[ptr_t]
            ptr_t += 1
            
        if s[i] == "?":
            s[i] = t[ptr_t]
            ptr_t += 1
            

        if ptr_t >= len(t):
            break

    if ptr_t < len(t):
        print("NO")
    else:
        print("YES")
        for val in s:
            if val == "?":
                print(dum,end='')
            else:
                print(val,end='')
        print()


    

            


#solve()  
for _ in range(T):
    solve() 
