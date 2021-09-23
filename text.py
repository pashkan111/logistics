

# def find_fib_numbers(count, lst):
#     lst = []
#     if count == 0:
#         return 0
#     elif count == 1:
#         return 1
#     else:
#         t = (find_fib_numbers(count-1, lst) + find_fib_numbers(count-2, lst))
#         return lst
    
# print(find_fib_numbers(7))

def find_fib_numbers(count):
    lst = []
    a = 0
    b = 1
    for i in range(count*2):
        a, b = b, a + b
        if a%2:
            continue
        lst.append(a)
    return lst

print(find_fib_numbers(7))

