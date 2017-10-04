# def power(num, power):
#     if num > power:
#         return num ** power
#     elif num < power:
#         return power ** num
#
#
# print(power(3,2))

# def evenodd(num):
#     if num % 2 == 0:
#         return(f"Your number {num} is Even")
#     else:
#         return (f"your number {num} is Odd")
#
# print(evenodd(6))
# def check():
#     li = [1,2,3,4,5,6,7,8,9,10]
#     even = []
#
#     for a in li:
#         if a % 2 == 0:
#             even.append(a)
#     return even
#
# print(check())

def quantity(num):
    li = range(1,num)
    even = []
    odd = []
    for i in li:
        if i % 2 == 0:
            even.append(i)
        if i % 2 != 0:
            odd.append(i)

    return len(even), len(odd)

x,y = quantity(101)
print(x)
print(y)

def sum(*args):
    s = 0
    for i in args:
        s = s+i
    return s
print(sum(2,3,4))
