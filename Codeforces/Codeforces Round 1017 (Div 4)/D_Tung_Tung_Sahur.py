from collections import defaultdict
from collections import deque
from collections import Counter
from itertools import permutations
from math import *
from bisect import *
from heapq import *
from types import GeneratorType
 
import sys
import random
 
# @bootstrap
#random.shuffle(a)
RANDOM = random.getrandbits(32)
 
class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc
input = lambda: sys.stdin.readline().rstrip("\r\n")
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lmii = lambda: list(map(int, input().split()))
tmii = lambda: tuple(map(int, input().split()))
mfi = lambda: map(float, input().split())
lmfi = lambda: list(map(float, input().split()))
MOD = 10**9 +7
T = ii()

def key_fn(x):
    return [x%ct]

def key_fn1(x):

    ct_z = 0
    while x%10 == 0 and x:
        ct_z += 1
        x //= 10

    return -ct_z


def sum_n(a,b):
    return max(0,( b*(b+1)//2)  - ((a-1)*(a)//2  ))

def exists(val,a,b):
    if  a <= val and val <= b:
        return 1
    return 0

def find_interval(arr, target):
    low, high = 0, len(arr) - 1
    
    # Handle edge cases where target is smaller than the smallest element
    # or larger than the largest element
    if target <= arr[low]:
        return None, arr[low]
    if target >= arr[high]:
        return arr[high], None
    
    while low <= high:
        mid = (low + high) // 2

        # If target is exactly at arr[mid]
        if arr[mid] == target:
            return arr[mid], arr[mid]

        # If target is between arr[mid] and arr[mid+1]
        if arr[mid] < target < arr[mid + 1]:
            return arr[mid], arr[mid + 1]

        # Narrow down the search interval
        if target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return None

def xor(arr):
    ans = 0
    for val in arr:
        ans ^= val
    return ans

def bin_val(val):
    i = 0
    string = ""
    while val>>i:
        string += str(val>>i&1)
        i += 1
    return string[::-1]



def find_mex(arr):
    """Find the minimum excludant (MEX) of an array."""
    arr_set = set(arr)  # Convert to a set for O(1) lookups
    mex = 0
    while mex in arr_set:
        mex += 1
    return mex



ct = 0

def dig_sum(n):
    res = 0
    while n:
        res += n%10
        n //= 10

    return res

def calc(arr,s,e):
    n = len(arr)
    return_val = 0

    
    for i in range(min(n-1,s),min(n-1,e)):
        return_val += abs(arr[i]-arr[i+1])
    return return_val

def manhattan(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

def slope(pt1,pt2):
    return (pt1[1]-pt2[1])/(pt1[0]-pt2[0])

def find_divisors(n):
    """
    Finds all divisors of a given number n in an efficient manner.

    :param n: The number to find divisors for.
    :return: A sorted list of divisors of n.
    """
    if n <= 0:
        raise ValueError("The number must be positive.")
    
    divisors = []
    sqrt_n = int(n**0.5)  # Calculate square root of n
    
    for i in range(1, sqrt_n + 1):
        if n % i == 0:  # If i is a divisor
            divisors.append(i)
            if i != n // i:  # Avoid adding the square root twice for perfect squares
                divisors.append(n // i)
    
    return sorted(divisors)


def is_point_rect(pt,pt1,pt2,corners):
    #pt -> point to be check if it is on a rectangle
    def above(pt1,pt2):
            slope = (pt2[1]-pt1[1]) /(pt2[0]-pt1[0])

            if pt[1]-pt1[1]-slope*(pt[0]-pt1[0]) >= 0:
                return 1

            else:
                return 0

    def below(pt1,pt2):
        slope = (pt2[1]-pt1[1]) /(pt2[0]-pt1[0])

        if pt[1]-pt1[1]-slope*(pt[0]-pt1[0]) <= 0:
            return 1

        else:
            return 0

    if above(corners[0],corners[1]) and above(corners[1],corners[2]) and below(corners[0],corners[3] ) and below(corners[3],corners[2]):
        print("YES")
    else:
        print("NO") 
def countDigit(n):
  
    # Base case
    if n == 0:
        return 1

    count = 0
    
    # Iterate till n has digits remaining
    while n != 0:
      
        # Remove rightmost digit
        n = n // 10
        
        # Increment digit count by 1
        count += 1

    return count

def pt_pos_line(pt1,pt2,pt3): #form eqn using pt1,pt2 and determin pos of pt3
        m = (pt2[1]-pt1[1])/(pt2[0]-pt1[0])
        res =  m*(pt3[0]-pt1[0])+pt1[1]
        if res == pt3[1]:
            return "on"
        elif pt3[1] > res :
            return "above"
        else:
            return "below"

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, limit + 1) if is_prime[p]]
    return primes
ct = 0

#PRIMES = sieve_of_eratosthenes(2*10**5)

def binaryTodecimal(n):
    decimal = 0
    power = 1
    while n>0:
        rem = n%10
        n = n//10
        decimal += rem*power
        power = power*2
        
    return decimal
def and_val(f,t,prefix):
        ret = 0
        ptr = 0
        for g,h in zip(prefix[t][::-1] , prefix[f-1][::-1] ):
            if g-h == t-f+1 :
                ret += 2**ptr
            ptr += 1

        return ret

def prefix_bits(n,a):
    prefix = [] 
    to_add = [0]*(30)
    for i in range(n):
        tmp = a[i]
        ptr = -1
        while tmp  :
            to_add[ptr] += tmp%2
            tmp //= 2
            ptr -= 1
        prefix.append(to_add[:])

    # print(prefix)
    prefix.append( [0]*30)
    return prefix

def product_of_digits(n):
    """Returns the product of digits of a number."""
    if n == 0:
        return 0  # Edge case: product of digits of 0 is 0
    
    product = 1
    n = abs(n)  # Handle negative numbers
    
    while n > 0:
        product *= n % 10  # Multiply last digit
        n //= 10  # Remove last digit
    
    return product



def ceil_fn(val):
    if val//2 - val/2 == 0:
        return val//2
    else:
        return (val//2) +1

def solve():
    global ct
    ct += 1
    s= input()
    d = input()
    n = len(s)
    m = len(d)
    ptr1,ptr2 = 0,0

    while ptr1 <  n and ptr2 < m:

        j = ptr1+1
        while j < n and s[j] == s[ptr1]:
            j += 1

        k = ptr2+1
        if d[ptr2] != s[ptr1]:
            print("NO"
                )
            return
        while k < m  and d[k] == d[ptr2]:
            k += 1


        bound = j-ptr1

        if  bound > k-ptr2 or 2*bound < k-ptr2 :
            print("NO")
            return
        ptr1 = j
        ptr2 = k
    if ptr2 == m and ptr1 == n:
        print("YES")
    else:
        print("NO")

    

















    

    
      



    

    

    

        






    

        
# solve()  
for _ in range(T):
    solve() 