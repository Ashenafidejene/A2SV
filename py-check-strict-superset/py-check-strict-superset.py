# Enter your code here. Read input from STDIN. Print output to STDOUT
A= set(map(int, input().split()))
N = int(input())
Flag = True
for i in range (N) :  
   otherSets= set(map(int, input().split()))
   is_superset = A >= otherSets
   if is_superset == False:
       Flag= False 
print(Flag)

   

