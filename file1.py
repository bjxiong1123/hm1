L,R = map(int,input().split())
def sqrt(x):
    a = x+1
    for i in range(0,21):
        a = (a+x/a)/2
    return a
def f(x):
    a = int(sqrt(x))
    num = 0
    for i in range(2,a+1):
        if x%i == 0:
            num += i+x//i
        else:
            continue
    if x%a == 0:
            num -= a
    return num+1
lis = []
for i in range(L,R+1):
    b = f(i)
    if f(b) == i and L<=b<=R:
        print(b)
        if lis.count(i) == 0 and b==i:
            continue
        elif lis.count(i) == 0:
            lis.append(i)
            lis.append(b)
        else:
            continue
ans = 0
for i in range(0 ,len(lis)):
    ans+=lis[i]
print(ans)
