number = input("Введите элементы списка, разделенные запятыми:")
numbers_list = number.split(',')
my_list = []
for number in numbers_list:
    if numbers_list.count(number) == 1:
        my_list.append(number)

print(my_list)