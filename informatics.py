# A. Линейный поиск - 1
# n = int(input())
# array = list(map(int, input().split()))
# search_number = int(input())
# count = 0
# for i in array: 
#     if search_number == i: 
#         count += 1 
# print(count)

# B. Линейный поиск - 2
# n = int(input())
# array = list(map(int, input().split()))
# search_number = int(input())
# result = "YES" if search_number in array else "NO"
# print(result)

# C. Ближайшее число
# n = int(input())
# array = list(map(int, input().split()))
# search_number = int(input())
# found_number = array[0]
# for i in range(len(array)): 
#     if abs(search_number - found_number) > abs(search_number - array[i]): 
#         found_number = array[i] 
# print(found_number)

# Задача №227. Максимальный элемент массива
# n = int(input())
# array = list(map(int, input().split()))
# max_element = array[0]

# for i in range(len(array)): 
#     if max_element < array[i]: 
#         max_element = array[i]

# print(max_element)

# Задача №228. Номер максимального элемента массива
n = int(input())
array = list(map(int, input().split()))
max_element = array[0]
max_element_index = 0 

for i in range(len(array)): 
    if max_element < array[i]: 
        max_element = array[i]
        max_element_index = i 

print(max_element_index+1)