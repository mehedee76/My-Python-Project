li = [23,12,34,66,77,23,3,4,98]
temp = 0
i = 0
while i < len(li):
    if li[i] > temp:
        temp = li[i]
    i+=1
print(temp)
