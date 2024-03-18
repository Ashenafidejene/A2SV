# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = map(int, input().split())
A = [(i + 1, input()) for i in range(n)]
B = [input() for i in range(m)]
listed = []
for val in B:
    for i in range(len(A)):
        if val == A[i][1]:
            listed.append(str(A[i][0]))
    if len(listed) != 0:
        print(' '.join(listed))
    else:
        print(-1)
    listed = []


    
    
