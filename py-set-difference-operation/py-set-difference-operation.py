# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))
k = a.difference(b)
print(len(k))