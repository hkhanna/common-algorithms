def bubble_sort(arr):
    """Bubble Sort, n^2, as inefficient as it gets"""
    swapped = True
    while swapped:
        swapped = False
        for index in range(len(arr) - 1):
            if arr[index] > arr[index + 1]:
                swapped = True
                arr[index], arr[index + 1] = arr[index + 1], arr[index]


def bubble_sort_improved(arr):
    """Bubble sort improved, triangular, doesn't redo sorted items"""
    swapped = True
    passes = 0
    while swapped:
        swapped = False
        passes += 1  # make it triangular instead of squared

        for index in range(len(arr) - passes):
            if arr[index] > arr[index + 1]:
                swapped = True
                arr[index], arr[index + 1] = arr[index + 1], arr[index]

def selection_sort(arr):
    """Selection Sort"""
    for passthrough in range(len(arr)):
        index_of_lowest_value = passthrough
        for index in range(passthrough, len(arr)):
            if arr[index] < arr[index_of_lowest_value]:
                index_of_lowest_value = index
        arr[passthrough], arr[index_of_lowest_value] = arr[index_of_lowest_value], arr[passthrough] 

algorithms = [
    bubble_sort,
    bubble_sort_improved,
    selection_sort
]