


data = [1,2,3,4]

set = [2,3]

def powerset(n):
    max = 1<<n
    for i in range(0,max):
        print('{',end=' ')
        for j in range(0,n):
            if ( (i & (1<<j)) != 0 ):
                print(data[j] , end=' ')
        print('}',end=' ')
    print(" ")
powerset(4)

print('----------------------------------------------')

from itertools import combinations
from collections import Counter

def subset(a,result,set):
    c=list(combinations(a,set))
    result +=c

    temp = []
    for i in range(0,len(result)):
        temp1 = ''
        for j in range(0,len(result[i])):
            temp1+=(result[i][j])
        temp.append(temp1)
    return temp


a = ['A','B','C']
c = ['B','D','G']
f = ['A','C','E','Q','X']
e = ['A','C','Q']
k = ['C','E','Q','X']
dic = {'a' : a, 'c': c, 'f': f, 'e' : e, 'k':k}
print(dic)
result = []

res = {}
for i in set:
    (subset(a,result,i))
    (subset(c,result,i))
    (subset(e, result, i))
    (subset(k, result, i))
    temp = subset(f,result,i)
    del result
    result = []
    #print(temp)
    res[i] = temp

print(res)

dic1={}
for i in set:
    count = Counter(res[i])
    dic1[i] = count.most_common()

print(dic1)

ans = {}
tempp = []
for i in set:
    for j in range(len(dic1[i])):
        if j == 0:
            max = dic1[i][j][1]
        if dic1[i][j][1] == max:
            tempp.append( dic1[i][j][0])
    ans[i] = tempp
    print(tempp)
    del tempp
    tempp=[]

print(ans)







