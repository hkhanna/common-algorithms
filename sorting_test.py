import random
import prettytable
from timeit import default_timer as timer
from sorting_algorithms import algorithms

def compare_sort(arr, *sort_fns):
    arr_sorted = sorted(arr)
    comparisons = {}
    for fn in sort_fns:
        test_arr = arr[:]
        if fn == sorted:
            key = "Built-in Sort"
        else:
            key = fn.__doc__
        start = timer()
        fn(test_arr)
        end = timer()
        comparisons[key] = end - start
        if fn != sorted and test_arr != arr_sorted:
            print(f"Incorrect Sorting\n{test_arr[:-5]}\n{arr_sorted[:-5]}")
            return
    return comparisons

sz = 1000
arr = list(range(sz))
arr = sorted(arr)
best_case = compare_sort(arr, *algorithms)

arr = list(range(sz))
random.shuffle(arr)
average_case = compare_sort(arr, *algorithms)

arr = list(range(sz))
arr = sorted(arr, reverse=True)
worst_case = compare_sort(arr, *algorithms)

table = prettytable.PrettyTable()

table.field_names = ["Algorithm", "Best Case", "Average Case", "Worst Case"]
algs = {}
for case in best_case, average_case, worst_case:
    for k, v in case.items():
        if k not in algs:
            algs[k] = []
        algs[k].append(f"{v:0.4f}")

for k, v in algs.items():
    v.insert(0, k)
    table.add_row(v)

print(table)
