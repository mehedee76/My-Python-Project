# L = [1, 2, 3, 4, 5, 6, 7]
# li = []
#
# for i in L:
#     if i % 2 == 1:
#         li.append(i)
#
# print(li)
#
#
# li = []
# for i in range(2000,3201):
#     if (i % 7 == 0) and (i % 5 == 0):
#         li.append(i)
# print(li)

def leap_year(year):
    x = 0
    while x < 20:
        if year % 4 != 0 and year % 400 != 0:
            year +=1
            print(f"{year} is a common year")

        elif year % 100 != 0:
            year +=1
            print(f"{year} is a leap year")
            x += 1


leap_year(2011)
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
#
marks = [45,23,12,54]
nmarks = []
for s in marks:
    nmarks.append(s)
i = sum(nmarks)
print(f"Sum = {i}")
# #
# #
# # marks = [45,23,12,54]
# # nmarks = []
# # for s in marks:
# #     nmarks.append(s)
# # i = min(nmarks)
# # print(f"Minimum number = {i}")
#
# string = ['abba','amma','vaia','apu','121']
# ctn = 0
# for nstring in string:
#     if len(nstring) > 1 and nstring[0] == nstring[-1]:
#         ctn += 1
# print(f"Total String = {ctn}")
#
# li = []
# if not li:
#     print("List is Empty!!")
# else:
#     print("List has elements.")
