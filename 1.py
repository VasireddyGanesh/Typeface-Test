num=int(input())
result=''
while num>0:
    rem = num%3
    num = num//3
    result = str(rem)+result
    
print(result)
