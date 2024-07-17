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
    n,k = mii()
    s = input()
    t = input()
    ct_zeros_s = 0
    diff_0 = 0
    diff_1 = 0
    ct_ones_s = 0
    ct_zeros_t = 0
    ct_ones_t = 0
    for a,b in zip(s,t):
        if a != b:
            if a == '0':
                diff_0 += 1
            if a == '1':
                diff_1 += 1
        if a == '0':
            ct_zeros_s += 1
        if a=='1':
            ct_ones_s += 1
        if b == '0':
            ct_zeros_t += 1
        if b =='1':
            ct_ones_t += 1

        
            
    if ct_zeros_s != ct_zeros_t or ct_ones_s != ct_ones_t :
        print("NO")
        return
    elif ct_ones_s == 1 and ct_zeros_s == 1:
        if s == t:
            if k % 2 == 0:
                print("YES")
                return
            else:
                print("NO")
                return
            
        else:
            if k % 2 == 1:
                print("YES")
            else:
                print("NO")

    else:
        
        if diff_1 > k:
            print("NO")
        else:
            print("YES")
            
        
for _ in range(T):
    solve() 

