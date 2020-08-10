# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
even=""
odd=""
for x in range(0,T):
    S = input()
    for i in range(0,len(S)):
        if i%2==0:
            even+=S[i]
        else:
            odd+=S[i]
    print(even,odd)   
    even=""
    odd=""         



