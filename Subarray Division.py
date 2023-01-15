def birthday(s, d, m):
    # Write your code here
    i=0
    ans =0
    if len(s)==1:
        if sum(s)== d:
            ans+=1
        return ans
    while i+m-1<len(s):
        print(s[i:i+m])
        if sum(s[i:i+m])== d:
            ans+=1
        i+=1
    print(ans)

s = list(map(int, input().rstrip().split()))

first_multiple_input = input().rstrip().split()

d = int(first_multiple_input[0])

m = int(first_multiple_input[1])


birthday(s,d,m)