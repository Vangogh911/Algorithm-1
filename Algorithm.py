import random


def sort(arr, n, i):
    largest = i  # Определяем наибольший элемент (корень)
    l = 2 * i + 1
    r = 2 * i + 2

    # Проверяем существует ли левый дочерний элемент больший, чем корень
    if l < n and arr[largest] < arr[l]:
        largest = l

    # Проверяем существует ли правый дочерний элемент больший, чем корень
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Заменяем корень, если нужно
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Применяем sort к корню.
        sort(arr, n, largest)


# Основная функция для сортировки массива заданного размера
def heap_sort(arr):
    n = len(arr)

    # Построение max-heap.
    for i in range(n, -1, -1):
        sort(arr, n, i)

    # Один за другим извлекаем элементы
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # свап
        sort(arr, i, 0)


# Управляющий код для тестирования
arr = []
for i in range(10):
    arr.append(random.randrange(100))
print("Sorce array is: ")
print(arr)
heap_sort(arr)
print("Sorted array is: ")
print(arr)
