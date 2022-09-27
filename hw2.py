'''5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.'''

from random import randint as r

my_int = int(input("Enter the number of elements in the array "))

my_list = []

for i in range(0, my_int):
    my_list.insert(r(0,my_int), i)

print(my_list)
print(sorted(my_list))