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
    
    
    n,k = mii()
    ct_alpha_a = [[0]*27]
    ct_alpha_b = [[0]*27]
    
    a = input()
    b = input()
    to_add = [0]*27
    for ind,val in enumerate(a):
        #print(ind+1,ord(val)-96)
        to_add[ord(val)-96] += 1
        ct_alpha_a.append(to_add[:])
    to_add = [0]*27
    for ind,val in enumerate(b):
        #print(ind+1,ord(val)-96)
        to_add[ord(val)-96] += 1
        ct_alpha_b.append(to_add[:])
    
    for _ in range(k):
        l,r = mii()
        min_op = 0
        for i in range(1,27):
            v1 = ct_alpha_a[r][i] - ct_alpha_a[l-1][i]
            v2 = ct_alpha_b[r][i] - ct_alpha_b[l-1][i]
            min_op += max(0,v1-v2)
        print(min_op)



#solve()  
for _ in range(T):
    solve() 
