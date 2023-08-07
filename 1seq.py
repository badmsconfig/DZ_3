#1
num_elements = int(input("Введите количество элементов списка: "))

my_list = []

for i in range(num_elements):
    try:
        element = int(input(f"Введите цифру {i + 1}: "))
        my_list.append(element)
    except ValueError:
        print("Неверный формат ввода. Введите целое число.")
my_list.sort()
print("Отсортированный список:", my_list)


#2
num_elements = int(input("Введите количество элементов в списке: "))
my_list = []

for i in range (num_elements):
    element = input(f"Введите число {i + 1}: ")
    if element.isdigit():
        my_list.append(int(element))

my_list.sort()
print("Сортированный список:", my_list)

