
import prettytable
from timeit import default_timer as timer
from data_structures import MyArray, PythonArray

def compare_read(index, *classes):
    comparisons = {}
    for c in classes:
        key = c.__class__.__name__
        start = timer()
        c.read(index)
        end = timer()
        comparisons[key] = end - start
    return comparisons

def compare_insert(val, index, *classes):
    comparisons = {}
    for c in classes:
        key = c.__class__.__name__
        start = timer()
        c.insert(val, index)
        end = timer()
        comparisons[key] = end - start
    return comparisons

def compare_search(val, *classes):
    comparisons = {}
    for c in classes:
        key = c.__class__.__name__
        start = timer()
        c.search(val)
        end = timer()
        comparisons[key] = end - start
    return comparisons

def compare_delete(index, *classes):
    comparisons = {}
    for c in classes:
        key = c.__class__.__name__
        start = timer()
        c.delete(index)
        end = timer()
        comparisons[key] = end - start
    return comparisons

myarray = MyArray(list(range(100)))
pyarray = PythonArray(list(range(100)))
classes = [myarray, pyarray]

read = compare_read(50, *classes)
insert_beginning = compare_insert("hello", 0, *classes)
insert_end = compare_insert("hello", -1, *classes)
search = compare_search("notexist", *classes)
delete_beginning = compare_delete(0, *classes)
delete_end = compare_delete(-1, *classes)

table = prettytable.PrettyTable()

table.field_names = ["Data Structure", "Read", "Insert (B)", "Insert (E)", "Search", "Delete (B)", "Delete (E)"]
ds = {}
for operation in [read, insert_beginning, insert_end, search, delete_beginning, delete_end]:
    for k, v in operation.items():
        if k not in ds:
            ds[k] = []
        ds[k].append(f"{v:0.7f}")

for k, v in ds.items():
    v.insert(0, k)
    table.add_row(v)

print(table)