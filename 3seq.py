input_str1 = input("Введите элементы 1-го списка через запятую: ")
list1 = [int(num) for num in input_str1.split(',')]

input_str2 = input("Введите элементы 2-го списка через запятую: ")
list2 = [int(num) for num in input_str2.split(',')]

result_list = [item for item in list1 if item not in list2]

print("Результат:", ', '.join(map(str, result_list)))