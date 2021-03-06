import random
import prettytable
from timeit import default_timer as timer
import data_structures as ds


def compare(classes, fn_name, *args):
    comparisons = {}
    for c in classes:
        key = c.__class__.__name__
        start = timer()
        res = c.call(fn_name, *args)
        end = timer()
        comparisons[key] = f"{end - start:0.7f}"
        if res == None:
            comparisons[key] = "N/A"
    return comparisons


rlist = list(range(10000))
hashdata = {k: k - 1 for k in range(1, 10000)}

classes = [
    ds.MyArray(rlist),
    ds.PythonArray(rlist),
    ds.MyStack(rlist),
    ds.MyQueue(rlist),
    ds.MyHashTable(hashdata),
    ds.PythonHashTable(hashdata),
    ds.MySet(rlist),
    ds.PythonSet(rlist),
    ds.MyOrderedArray(rlist),
    ds.MyLinkedList(rlist),
    ds.MyDoublyLinkedListQueue(rlist),
    ds.MyBST(),
    ds.MyMaxHeap(),
    ds.MyTrie()
]

read = compare(classes, "read", 50)
insert_beginning = compare(classes, "insert", "hello", 0)
insert_end = compare(classes, "insert", "hello", -1)
search = compare(classes, "search", "notexist")
delete_beginning = compare(classes, "delete", 0)
delete_end = compare(classes, "delete", -1)
add = compare(classes, "add", 5)
remove = compare(classes, "remove")

table = prettytable.PrettyTable()

table.field_names = [
    "Data Structure",
    "Read",
    "Insert (B)",
    "Insert (E)",
    "Search",
    "Delete (B)",
    "Delete (E)",
    "Add",
    "Remove",
]
structs = {}
for operation in [
    read,
    insert_beginning,
    insert_end,
    search,
    delete_beginning,
    delete_end,
    add,
    remove,
]:
    for k, v in operation.items():
        if k not in structs:
            structs[k] = []
        structs[k].append(v)

for k, v in structs.items():
    v.insert(0, k)
    table.add_row(v)

print(table)