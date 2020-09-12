
# kakao num1

temp = input()

temp = temp.lower()

temp = list(filter(lambda a : a!='.',temp))

print(''.join(temp))