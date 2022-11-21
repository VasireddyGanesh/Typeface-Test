input_string1 , input_string2 = list(input().split(",")) # 2 input strings should be seperated by comma
count=0
for i in input_string1:
    if i==input_string2[-1]:
        count+=1
print(count)
