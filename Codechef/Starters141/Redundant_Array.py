from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    freq = defaultdict(int)
    for val in a:
        freq[val] += 1
        

    #print(freq)
    min_cost = float('inf')
    for i in freq:
        min_cost = min(min_cost,(n-freq[i])*i)
        
    print(min(n,min_cost))
        
    
