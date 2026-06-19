import time
from sort import sort


def make_orders(n):
    orders = []
    for i in range(n):
        orders.append({"id": i, "price": n - i})
    return orders


sizes = [100, 500, 700]
algos = ["quick", "insert", "merge"]

for n in sizes:
    print(f"N = {n}:")
    for algo in algos:
        data = make_orders(n)
        t1 = time.time()
        sort(data, by="price", algo=algo)
        t2 = time.time()
        print(f"  {algo}: {(t2 - t1) * 1000} ms")
    print()
