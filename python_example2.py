
# kakao num1

temp = "input()"

temp = temp.lower()

temp = list(filter(lambda a : a!='.',temp))

print(''.join(temp))


text = "fuck you"

for i in range(len(text)):
    print(text[i::-2]) # i번째부터 뒤로 두칸씩 띄어서
    ## ::  두칸씩 띄워서 진행

for i in range(len(text)):
    print(text[i:-2]) ## i:-a 는 i부터 뒤에서a번째까지
                      ## i:a 는 1부터 앞에서 a번째까지


data = [1,2,3,4]

def powerset(n):
    max = 1<<n
    for i in range(0,max):
        print('{',end=' ')
        for j in range(0,n):
            if ( (i & (1<<j)) != 0 ):
                print(data[j] , end=' ')
        print('}',end=' ')

powerset(4)

