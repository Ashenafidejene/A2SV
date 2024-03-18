# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
set2 = set(map(int, input().split()))
m = int(input())
set1 = set(map(int, input().split()))
union_set = set1 | set2
print(len(union_set))