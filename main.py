# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в списке A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     3
# #     -> 1

# some_list = []
# N = int(input('Введите кол-во элементов списка: '))
# for _ in range(N):
#     number = int(input())
#     some_list.append(number)

# X = int(input('Введите число X: '))

# count = 0

# for i in some_list:
#     if i == X:
#         count += 1
# print (count)





# Задача 18: Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

some_list = []
N = int(input('Введите кол-во элементов списка: '))
for _ in range(N):
    number = int(input())
    some_list.append(number)

X = int(input('Введите число X: '))

for ind in range(len(some_list)-1):

    if X < some_list[0]:
        print (some_list[0])
        break

    if X > some_list[N-1]:
        print (some_list[N-1])
        break  

    if some_list[ind] < X < some_list[ind + 1]:
        if some_list[ind + 1] - X > X - some_list[ind]:
            print (some_list[ind])
        else:
            print(some_list[ind + 1])

