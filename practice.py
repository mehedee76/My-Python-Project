# li = []
# for i in range(1500,2701):
#     if (i % 7 == 0) and (i % 5 == 0):
#         li.append(i)
# s = sum(li)
# x = min(li)
# print(s)
# print(x)

# import random
# while True:
#     num = int(input("Enter a number: "))
#     num2 = random.randint(0,10)
#     print (num2)
#
#     if num2 == num:
#
#         print(f"Guessed number is {num}")
#         break

# marks = [45,23,12,54]
# nmarks = []
# for s in marks:
#     nmarks.append(s)
# i = sum(nmarks)
# print(f"Sum = {i}")
#
#
# marks = [45,23,12,54]
# nmarks = []
# for s in marks:
#     nmarks.append(s)
# i = min(nmarks)
# print(f"Minimum number = {i}")

string = ['abba','amma','vaia','apu','121']
ctn = 0
for nstring in string:
    if len(nstring) > 1 and nstring[0] == nstring[-1]:
        ctn += 1
print(f"Total String = {ctn}")

li = []
if not li:
    print("List is Empty!!")
else:
    print("List has elements.")
