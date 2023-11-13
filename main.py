def insertion_sort(arr):
    comparisons = 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            comparisons += 1
        arr[j + 1] = key
    return comparisons

# Чтение массива из файла input.txt
with open('input.txt', 'r') as file:
    array = [int(num) for num in file.readline().split()]

# Сортировка массива вставками
comparisons = insertion_sort(array)

# Запись отсортированного массива и числа сравнений в файл output.txt
with open('output.txt', 'w') as file:
    file.write(' '.join([str(num) for num in array]) + '\n')
    file.write(str(comparisons))
