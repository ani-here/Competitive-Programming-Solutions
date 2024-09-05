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
    n = ii()
    a = lmii()
    if a.count(0) == n:
        print(n*(n-1)//2)
        return
    freq = defaultdict(int)
    max_oc = 0
    max_no= -1
    for val in a:
        freq[val] += 1
        if val != 0 and freq[val] > max_oc:
            max_oc = freq[val]
            max_no = val
    
    for i in range(n):
        if a[i] == 0:
            a[i] = max_no
    ans = 0  
    freq[max_no] += freq[0]
    #print(freq)
    for val in freq:
        if val != 0:
            ans += freq[val]*(freq[val]-1)//2
    print((ans))
        


#solve()  
for _ in range(T):
    solve() 
