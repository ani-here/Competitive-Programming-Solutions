t = int(input())
for _ in range(t):
    la,lb = map(int,input().split())
    a = input()
    b = input()
    min_ham = float('inf')
    for i in range(la-lb+1):
        curr_dist = 0
        for k in range(lb):
            if a[i+k] != b[k]:
                curr_dist += 1
        min_ham = min(min_ham,curr_dist)
        
    print(min_ham)
        
        
            
        
        
        
        
