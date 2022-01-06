
def solution(n,m,k,numlist):
    numList.sort(reverse=True) # 큰수부터
    max=0
    cnt=0
    while cnt<=n :
        for i in range(k):
            max+=numList[0]
            cnt+=1
        max+=numList[1]
        cnt+=1
    return print(max)

n,m,k=map(int,input().split())
numList = list(map(int, input().split()))
solution(n,m,k,numList)
